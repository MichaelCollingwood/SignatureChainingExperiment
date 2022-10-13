import React, { useState } from 'react';
import Message from '../components/Message';

type Message = {
    data: string,
    validSources: string[]
}

export default function Messages() {
    const [messages, setMessages] = useState<Message[]>([])

    return (
        <div>
            <ul>
                <Message />
                <Message />
                <Message />
            </ul>
        </div>
    );
}