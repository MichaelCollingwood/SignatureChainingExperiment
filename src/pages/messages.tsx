import React, { useState } from 'react';
import { Header } from '../components/Head';
import Message from '../components/Message';
import { Navbar } from '../components/NavBar';

type Message = {
    text: string,
    sources: string[]
}

export default function Messages() {
    const [messages, setMessages] = useState<Message[]>([
        {text: 'hello', sources:['a']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}, {text: 'world', sources:['a', 'b']}
    ])

    return (
        <div className='flex flex-col h-screen'>
            <Header />
            <Navbar />
            <ul className='bg-slate-200 m-4 rounded p-2 overflow-y-scroll'>
                {messages.map((message) => 
                    <Message text={message.text} sources={message.sources}/>
                )}
            </ul>
        </div>
    );
}