import React, { useState } from 'react';
import { Header } from '../components/Head';
import { Messages } from '../components/Messages';
import { Navbar } from '../components/NavBar';

export type MessageContent = {
    text: string,
    sources: string[]
}

type UserMessageRepository = {
    [peerId: string]: MessageContent[]
}

export default function MessagePage() {
    const [userMessageRepository, setMessageRepository] = useState<UserMessageRepository>()

    // useEffect fetch statement...
    // run server which initialises python server

    return (
        <div className='flex flex-col h-screen'>
            <Header />
            <Navbar />
            <Messages messages={userMessageRepository?.[peerId]}/>
        </div>
    );
}