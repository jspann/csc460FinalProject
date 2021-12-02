import { FileDrop } from "react-file-drop";
import "../app-copy.css";

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
          onFrameDrop={(event) => console.log("onFrameDrop", event)}
          onDragOver={(event) => console.log("onDragOver", event)}
          onDragLeave={(event) => console.log("onDragLeave", event)}
          onDrop={(files, event) => console.log("onDrop!", files, event)}
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
