import React, {useState} from 'react';
import intentsData from '..'

function Chat(){
    const[userInput, setUserInput] = useState('');
    const[chatMessages, setMessage] = useState([]);
    const[intents, setIntents] = useState(intentsData)

    const handleSubmit = (e) =>{
        e.preventDefault(); 

    const userMessage = userInput.trim().toLowerCase();
    const botResponse = intents.find((intent) => intent.patterns.some((pattern)=> user)

    }


}