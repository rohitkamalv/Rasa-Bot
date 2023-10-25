//Text to speech
const utter = window.speechSynthesis ;

function tts(text) {
    text = new SpeechSynthesisUtterance(text);
    utter.speak(text);

}

function getresp(transcript) {
    fetch("/", {
        method :"POST",
        body : JSON.stringify({ voice : true , user : transcript }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((response) => response.json())
    .then((json) => tts(json.text))
    }

console.log("test")
//Speech to Text
const recognition = new webkitSpeechRecognition();
recognition.lang = "en-US";
recognition.continuous = false;
recognition.interimResults = false;

function stt() {
    console.log("stt called")
    alert("start speaking")
    recognition.start();
    console.log("Listening");
    recognition.onresult = (event) => {
        var transcript = event.results[0][0].transcript;
        console.log("transcript -> ",transcript);
    getresp(transcript)
    
}}

document.getElementById("voicebtn").addEventListener('click',stt,true)
