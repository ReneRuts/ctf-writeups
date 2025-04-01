import asyncio
import re
import telnetlib3

HOST = "192.168.16.109"
PORT = 3141

def solve_math_question(question):
    match = re.match(r'What is (\d+)\s*([+\-*/])\s*(\d+)\?', question)
    
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
    return "Error: Invalid question"

async def handle_question(reader, writer):
    question = await reader.readuntil(b"?")
    question = question.decode('ascii').strip()
    
    if not question:
        return None
    
    answer = solve_math_question(question)
    print(f"Answer: {answer}")
    
    writer.write(f"{str(answer)}\n")
    await writer.drain()

    feedback = await reader.readuntil(b"left.")
    print(f"Feedback: {feedback.decode('ascii')}")
    
    return feedback

async def telnet_session():
    try:
        reader, writer = await telnetlib3.open_connection(HOST, PORT)
        print(f"Connected to {HOST}:{PORT}")
        
        welcome_message = await reader.readuntil(b"\n")
        print(f"Received welcome message:\n{welcome_message.decode('ascii')}")
        
        while True:
            feedback = await handle_question(reader, writer)
            
            if "Time's up!" in feedback.decode('ascii'):
                print("Time's up! We took too long.")
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if writer:
            writer.close()

if __name__ == "__main__":
    asyncio.run(telnet_session())