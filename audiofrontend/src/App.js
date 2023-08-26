import './App.css';
import {useState,useEffect} from 'react'

function App() {
  return (
    <div className="App">
      <h1>Audio Dashboard</h1>
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

useEffect(()=>{get()},[])
  return(
    <>
    <h1>hello</h1>
    <div className="frm">
      {/* using form to take input audio file from user */}
      <form >             
        <input type="file" onChange={(e)=>setAud(e.target.files[0])} />    {/* as soon as we upload audio file it saves in aud variable with the help of usestate */}
        <button type='button' onClick={fn}>Add</button>     {/* when we submit the form it is redirecting to function fn */}
      </form>
      {
        dt.map((data)=>{
          const {name,date,duration,size,extension,audio}=data
          return(
            <>
            <h3>{name}---{date}--{duration}---{size}---{extension}</h3>
            <audio src={audio} controls/>
            </>
          );
        })
      }
    </div>
    </>
  );
}


export default App;
