import { MessageContent } from "../pages/messages/[peerId]";

export default async (peerId: string): Promise<MessageContent[]> => {
  const response = await fetch(`http://localhost:8000/${peerId}`);
  return await response.json();
};
