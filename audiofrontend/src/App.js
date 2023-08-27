import './App.css';
import {useState,useEffect} from 'react'

function App() {
  return (
    <div className="App">
      <h1 className='heading'>Audio Player</h1>
      <Audio/>
    </div>
  );
}

function Audio()
{
  const [aud,setAud]=useState('');    {/* this hook is used to save the audio file */}
  const [msg,setMsg]=useState('') ;   {/* this hook is used to save any msg comming from the backend */}
  console.log(aud);
  console.log(msg);
let url="http://127.0.0.1:8000/song/";
{/* this is a post function and with the help of this function we will post the data to the database */}

let post=async()=>{
  let formdata = new FormData();
  formdata.append('audio',aud);
  console.log(formdata);
  let x=await fetch(url,{
    method:"post",
    body:formdata,
  });
  let y= await x.json();
  setMsg(y);
{/* after snding audio file to the database we are fetching the updated data from the database */}
  get();   
}

let fn=(e)=>{
  e.preventDefault();   {/* this function is calling post function for sending audio to the database */}
  post();
}

const [dt,setDt]=useState([]);  {/* this hook will save all the data fetched from the backend to be viewed in the frontend */}
{/* get function is used to fetch all the audio and their metadata from database */}
const get=async ()=>{          
    let f=await fetch(url);
    let data=await f.json();
{/* after fetching all the data from database it is saving the data in dt variable with the help of setDt hook */}
    setDt(data)    ;

  }
  console.log(dt);

useEffect(()=>{get()},[]) ;   {/* we have passed get function in the useeffect hook so with the help of this at the time of startup it is fetching all the data initilally */}

const dlt=async(id)=>{
  let url=`http://127.0.0.1:8000/song/${id}/`;
    await fetch(url,{
      method:"delete"
    })
    get()

  }
return(
    <div className='main'>
    <div className="frm">
      <h2>Upload a song here</h2>
      {/* using form to take input audio file from user */}
      <form >             
        <input type="file" onChange={(e)=>setAud(e.target.files[0])} />    {/* as soon as we upload audio file it saves in aud variable with the help of usestate */}
        <button type='button' onClick={fn}>Add</button>     {/* when we submit the form it is redirecting to function fn */}
      </form>
      </div>
      <div className="songs">
      {
        dt.map((data)=>{
          const {id,name,date,duration,size,extension,audio}=data
          return(
            <div className='songcolumn'>
            <h4  id='sname' className='attr'>{name}</h4>
            <h4 className='attr'>Duration:- {duration} minutes</h4>
            <h4 className='attr'>Size:- {size} mb</h4>
            <h4 className='attr'>Extension of file:- {extension}</h4>
            <h4 className='attr'>Date uploaded:- {date}</h4>
            <button type="button" onClick={()=>dlt(id)}>Delete</button>
            <br />
            {/* <br /> */}
            <audio src={audio} controls/>
            </div>
          );
        })
      }
      </div>
    </div>
  );
}


export default App;
