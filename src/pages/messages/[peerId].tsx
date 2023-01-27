import { useRouter } from 'next/router';
import React, { useEffect, useState } from 'react';
import fetchMessages from '../../client/fetchMessages';
import { Header } from '../../components/Head';
import { Messages } from '../../components/Messages';
import { Navbar } from '../../components/NavBar';

export type MessageContent = {
    text: string,
    sources: string[]
};

export default function MessagePage() {
    const router = useRouter();
    const [messages, setMessages] = useState<MessageContent[]>([])

    useEffect(() => {
        fetchMessages(router.query['peerId'] as string)
            .then((fetchedMessages) => { setMessages(fetchedMessages) })
            .catch((error) => {
                console.log(error);
                router.push('/error');
            });
    })

    return (
        <div className='flex flex-col h-screen'>
            <Header />
            <Navbar />
            <Messages messages={messages}/>
        </div>
    );
}