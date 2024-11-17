import React from "react";
import React, {useState} from "react";
import "./App.css";

function ChatComponent() {
    const [isOpen, setisOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const toggleChat = () => {
        setIsOpen(!isOpen);
    };

    const sendMessage = () => {
        if (input.trim() === "") return;
        setMessages([...messages, input]);
        setInput("");
    };

    return (
        <div className="chat">
            <button autofocus="button">Chat Here!</button>

        </div>
    )
}