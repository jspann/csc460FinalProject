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
			self.getVegetationImage(colorized_preds)
			return colorized_preds

	def getVegetationImage(self, colored_img):
		print("vege")
		print(type(colored_img))
		print(colored_img)
		cv_im = np.asarray(colored_img)
		cv_img = cv2.cvtColor(cv_im, cv2.COLOR_RGB2BGR)
		cv2.imwrite("job.png",cv_img)
		# print(np.unique(cv_img[:,:][0]))
		# print(np.unique(cv_img[xx,yy][0]))
		all_g = []
		for xx in range(cv_img.shape[0]):
			for yy in range(cv_img.shape[1]):
				# print(cv_img[xx,yy])
				all_g.append(cv_img[xx,yy])
				# if cv_img[xx,yy][0] == 
		print(np.unique(all_g))


		return

	def findSegmentsInImage(self):
		return

	def removeVegetationFromImage(self):
		return

iiimg = Image.open("testimg.JPG").convert('RGB')
cm = climate_model()
cm.loadInitialImage(img_arr=iiimg)