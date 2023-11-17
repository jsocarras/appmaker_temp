import '../App.css';
import React, {useState} from 'react';

const ChatDev = () => {
const [PromptUploaded, SetPromptUpload ] = useState(null);
const [NameUploaded, setNameUploaded] = useState();
const [convoValues, setConvoValues] = useState([]);
const [isUploaded, setIsUploaded] = useState(false);


const promptUploaded = (event) => {
   
    SetPromptUpload(event.target.value);
    
}
const NameUpload = (event) => {
   
    setNameUploaded(event.target.value);
    
}

const handleFileSubmission = () => {
  console.log("HIT")
  console.log('Current URL:', window.location.href);
  console.log(NameUploaded)
  if(PromptUploaded && NameUploaded)
  setIsUploaded(true)
  const fileForm = new FormData(); // Create a new FormData object
  fileForm.append('desc', PromptUploaded)
  fileForm.append('name', NameUploaded)
  console.log('FormData contents:', [...fileForm.entries()]);
  setConvoValues([...convoValues, 'loading', 'This may take awhile']);




  fetch('http://localhost/start', {
    method: 'POST',
    body: fileForm,
  })
  .then((response) => response.text())
  .then((data) => {
   
    setConvoValues([...convoValues, data]);
  
    console.log(data);
  })
  .catch((error) => {
    console.error('Error:', error);
    setConvoValues([...convoValues, error]);
  });
}

const handleDownload = async () =>{

try {
const response =  await fetch('http://localhost/download_zip', {
method: 'GET',
});

if(response.ok){
  const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);

      // Create a link element to trigger the download
      const link = document.createElement('a');
      link.href = url;
      link.download = 'downloaded-file.zip'; // Set the desired filename
      document.body.appendChild(link);
      link.click();
      window.URL.revokeObjectURL(url);
}
else{
  console.error('Download request failed with status:', response.status);
}
}
catch (error) {
  console.error('Error Downloading File: ', error)
}
}


  return (
    <>
        {isUploaded ? (
          // This is what you see when you upload files
        <div className='convo-section mx-auto' style={{overflow: "initial"}}>
        <div id='CloneGPT-convo-element'>
          <div className='w-100 file-upload-info d-flex justify-content-center mb-3'>

            <p className='m-3 p-0'>
              Succesfully Uploaded File(s)
            </p>
            <div className='query-input d-flex'>
            <button type="button" className='btn btn-secondary moveRight orange' onClick={handleDownload} >Download</button>
            </div>
          </div>
          {convoValues.map((convoText, convoNum) => (
            convoNum % 2 === 3 ? (
              <div key={convoNum} className='convo-bubble float-end query-text mb-3'>
                <p className='convo-bubble float-end query-text mb-3'>
                
               {convoText} 
                </p>
              </div>
            ) : (
              <div key={convoNum} className='convo-bubble float-start response-text mb-3 '>
                <p className='convo-content'>
                  {convoText === 'loading' ? (
                    <div class="spinner-border text-secondary d-flex justify-content-center" role="status">
                      <span class="visually-hidden">Loading...</span>
                    </div>
                  ): (
                    
                    convoText

              
                  
                  
                  
                  )}
           
                </p>
                
              </div>
              
            )))}
                        
        </div>
       
      </div>
      ): (
        // This is the page that you see on startup
        <div className='d-flex flex-column' style={{margin:"150px 0 0 0"}}>
          <div className='d-flex justify-content-center'>
            <p style={{color: "white"}}>Project Name</p>
          </div>
          <div className='form-floating mb-3' >
              <input id='myNameInput' className="form-control moveRight" name="nameInput" onChange={NameUpload}  type="text" placeholder='Ask me a question!'/>
              <label htmlFor="myNameInput" className ="moveRight">Project Name</label>
            </div>
          
          <div className='d-flex justify-content-center' style={{padding:"50px 0 0 0"}}>
            <p style={{color: "white"}}>Project Description</p></div>
            <div className='form-floating mb-3' >
              <input id='myNameInput' className="form-control moveRight" name="nameInput" onChange={promptUploaded}  type="text" placeholder='Ask me a question!'/>
              <label htmlFor="myNameInput" className ="moveRight">Prompt Description</label>
            </div>

          <div className='query-input d-flex'>
          
          <button type="button" className='btn btn-secondary moveRight'onClick={handleFileSubmission} >Submit</button>
        </div>
          

         


        </div>
      )}
      
    
   

      

     

    </>
  );
}

export default ChatDev;
