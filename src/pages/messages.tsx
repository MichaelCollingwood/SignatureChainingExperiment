import React, { useState } from 'react';
import { Header } from '../components/Head';
import Message from '../components/Message';
import { Navbar } from '../components/NavBar';

type Message = {
    text: string,
    sources: string[]
}

export default function Messages() {
    const [messages, setMessages] = useState<Message[]>([{text: 'hello', sources:['a']}, {text: 'world', sources:['a', 'b']}])

    return (
        <div>
            <Header />
            <Navbar />
            <ul className='bg-slate-200 p-2'>
                {messages.map((message) => 
                    <Message text={message.text} sources={message.sources}/>
                )}
            </ul>
        </div>
    );
}