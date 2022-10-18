export default function Message({ text, sources }: { text: string, sources: string[] }) {
    return (
        <li className='m-2 bg-yellow-300 rounded-lg px-3 py-2 flow-root max-w-sm'>
            <p className='float-left'>
                {text}
            </p>
            <p className='float-right'>
                {sources.join(', ')}
            </p>
        </li>
    )
}