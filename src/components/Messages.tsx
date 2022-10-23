import { MessageContent } from "../pages/messages"
import Message from "./Message"

type MessagesProps = { messages: MessageContent[] }

export function Messages({ messages }: MessagesProps) {

    return (
        <ul className='bg-slate-200 m-4 rounded p-2 overflow-y-scroll'>
            {messages.map((message) => 
                <Message text={message.text} sources={message.sources}/>
            )}
        </ul>
    )
}