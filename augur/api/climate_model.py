"""
Requires tensorflow 1.5.0 (any higher above 1.7.0 will no work with the model and above 1.5.0 will not work with m1)
"""



from torch.utils.data import dataset
from tqdm import tqdm
import network
import utils
import os
import cv2
import random
import argparse
import numpy as np

from torch.utils import data
from datasets import VOCSegmentation, Cityscapes, cityscapes
from torchvision import transforms as T
from metrics import StreamSegMetrics

import torch
import torch.nn as nn

from PIL import Image
# import matplotlib
# import matplotlib.pyplot as plt
from glob import glob


# For inpaint model
import tensorflow as tf
import neuralgym as ng
from inpaint_model import InpaintCAModel



class climate_model(object):
	"""
	This is a class for calling the functions associated with augUR's climate model.
	"""
	def __init__(self):
		super(climate_model, self).__init__()
		self.torch_device = "cpu"
		self.output_stride = 16
		self.num_classes = 19

		
	def loadInitialImage(self,img_arr):
		# image_files.append(opts.input)
		decode_fn = Cityscapes.decode_target

		model = network.modeling.__dict__["deeplabv3plus_mobilenet"](num_classes=self.num_classes, output_stride=self.output_stride)
		utils.set_bn_momentum(model.backbone, momentum=0.01)
	
		checkpoint = torch.load("model_stuff/best_deeplabv3plus_mobilenet_cityscapes_os16.pth", map_location=torch.device('cpu'))
		model.load_state_dict(checkpoint["model_state"])
		model = nn.DataParallel(model)
		model.to(self.torch_device)
		del checkpoint

		transform = T.Compose([
				T.ToTensor(),
				T.Normalize(mean=[0.485, 0.456, 0.406],
								std=[0.229, 0.224, 0.225]),
			])

		# TODO: where to Save results
		with torch.no_grad():
			model = model.eval()


			# img = Image.open(img_path).convert('RGB')
			img = img_arr
			img = transform(img).unsqueeze(0) # To tensor of NCHW
			img = img.to(self.torch_device)

			pred = model(img).max(1)[1].cpu().numpy()[0] # HW
			colorized_preds = decode_fn(pred).astype('uint8')
			colorized_preds = Image.fromarray(colorized_preds)
			# if opts.save_val_results_to:
			#     colorized_preds.save(os.path.join(opts.save_val_results_to, img_name+'.png'))
			colorized_preds.save(os.path.join("generated_image.png"))
			return colorized_preds

	def getVegetationImage(self, original_arr, colored_img):
		print("vege")
		print(type(colored_img))
		print(colored_img)
		cv_im = np.asarray(colored_img)
		original_arr = np.asarray(original_arr)
		original_arr = cv2.cvtColor(original_arr, cv2.COLOR_RGB2BGR)

		cv_img = cv2.cvtColor(cv_im, cv2.COLOR_RGB2BGR)
		'''
		# print(np.unique(cv_img[:,:][0]))
		# print(np.unique(cv_img[xx,yy][0]))
		# all_g = []
		# for xx in range(cv_img.shape[0]):
			# for yy in range(cv_img.shape[1]):
				# print(cv_img[xx,yy])
				# all_g.append(cv_img[xx,yy])
				# if cv_img[xx,yy][0] == 
		# print(np.unique(all_g))
		'''
		generated_mask = np.zeros(cv_img.shape)
		# generated_filtered_image = np.zeros(cv_img.shape)
		# gfi_a = cv2.cvtColor(generated_filtered_image, cv2.COLOR_RGB2RGBA)
		blank_image = np.zeros((cv_img.shape[0],cv_img.shape[1],3), np.uint8)
		rgba = cv2.cvtColor(blank_image, cv2.COLOR_RGB2RGBA)


		for xx in range(cv_img.shape[0]):
			for yy in range(cv_img.shape[1]):
				if cv_img[xx,yy][1] == 142:
					generated_mask[xx,yy,:] = [255,255,255]
					# gfi_a[xx,yy,:] = [255,255,255,255]
					rgba[xx, yy, :] = 255
				else:
					generated_mask[xx,yy,:] = original_arr[xx,yy, :]
					# generated_filtered_image[xx,yy,:] = [255,255,255]
					# gfi_a[xx,yy,:] = [0,0,0,0]
					rgba[xx, yy, :] = 0
		cv2.imwrite("masked_image.png", generated_mask)
		cv2.imwrite("generated_mask.png",rgba)
		return generated_mask, rgba

	def findSegmentsInImage(self):
		return

	def removeVegetationFromImage(self):
		return

	def inpaintImage(self,image,mask):
		FLAGS = ng.Config('inpaint.yml')
		checkpoint_dir = "model_logs/release_places2_256_deepfill_v2"
		model = InpaintCAModel()
		# image = cv2.imread(args.image)
		# mask = cv2.imread(args.mask)
		mask = cv2.cvtColor(mask, cv2.COLOR_RGBA2BGR)
		assert image.shape == mask.shape

		h, w, _ = image.shape
		grid = 8
		image = image[:h//grid*grid, :w//grid*grid, :]
		mask = mask[:h//grid*grid, :w//grid*grid, :]
		print('Shape of image: {}'.format(image.shape))

		image = np.expand_dims(image, 0)
		mask = np.expand_dims(mask, 0)
		input_image = np.concatenate([image, mask], axis=2)

		sess_config = tf.ConfigProto()
		sess_config.gpu_options.allow_growth = True
		with tf.Session(config=sess_config) as sess:
			input_image = tf.constant(input_image, dtype=tf.float32)
			output = model.build_server_graph(FLAGS, input_image)
			output = (output + 1.) * 127.5
			output = tf.reverse(output, [-1])
			output = tf.saturate_cast(output, tf.uint8)
			# load pretrained model
			vars_list = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
			assign_ops = []
			for var in vars_list:
				vname = var.name
				from_name = vname
				var_value = tf.contrib.framework.load_variable(checkpoint_dir, from_name)
				assign_ops.append(tf.assign(var, var_value))
			sess.run(assign_ops)
			print('Model loaded.')
			result = sess.run(output)
			cv2.imwrite("finalimage.jpg", result[0][:, :, ::-1])

		return

# iiimg = Image.open("testimg.JPG").convert('RGB')
# iiimg = Image.open("nycoutside.jpg").convert('RGB')
# iiimg = Image.open("/Users/jspann/Desktop/cityscapes/leftImg8bit/train/aachen/aachen_000002_000019_leftImg8bit.png").convert('RGB')
# iiimg = Image.open("test_outside.jpg").convert('RGB')

# cm = climate_model()
# colored_img = cm.loadInitialImage(img_arr=iiimg)
# gen_mask, rgba = cm.getVegetationImage(original_arr=iiimg, colored_img=colored_img)
# cm.inpaintImage(gen_mask,rgba)


