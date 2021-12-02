import { FileDrop } from "react-file-drop";
import "../app-copy.css";
/*
function setPhotoFormData(){
  var data = new FormData();
  const payload = {
      // id: self.refs.id,
      // studentName: self.refs.sname,
      // age: self.refs.age,
      // emailId: self.refs.emailId
      // original_image: 

  };
  data.append("myjsonkey", JSON.stringify(payload));
  return data;
}*/

function CrystalBall() {
  // const fileInputRef = useRef(null);
  // const onFileInputChange = (event) => {
  //   const { files } = event.target;
  //   // do something with your files...
  // }
  // const onTargetClick = () => {
  //   fileInputRef.current.click()
  // }
  return (
    <div className="page">
      <div className="cb">
        <FileDrop
          onFrameDragEnter={(event) => console.log("onFrameDragEnter", event)}
          onFrameDragLeave={(event) => console.log("onFrameDragLeave", event)}
          onFrameDrop={(event) => {}}
          onDrop={(files, event) => {
            console.log('onDrop!', files, event);
            console.log(typeof(files[0]));
            event.preventDefault();

            var data = new FormData();
            const payload = {
            // id: self.refs.id,
            // studentName: self.refs.sname,
            // age: self.refs.age,
            // emailId: self.refs.emailId
              whoami: "crystalball"

            };
            data.append("myjsonkey", JSON.stringify(payload));
            // data.append("file", files[0]);
            for (let i = 0; i < files.length; i++) {
              console.log("looping!");
            data.append(`images[${i}]`, files[i]);
            }

            // console.log("heart:",data);

              // Send POST
              fetch('/submitPhoto', {
                method: 'POST',
                body: data
              }).then(function(response) {
                if(response.ok) {
                 return alert("And the server replied:",response);
               }
             });
            }
          }

        >
          <div className="__act crys">
            drop a photo of your home into the crystal and we’ll show you
            <a href="/CrystalBallWorking">\
            {/* <input onChange={onFileInputChange} ref={fileInputRef} type="file" className="__crysbtn" >
              See My Future?
            </input> */}
            </a>
          </div>
        </FileDrop>
      </div>
    </div>
  );
}

export default CrystalBall;
