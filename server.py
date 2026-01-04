# hola Vicente Max ¿ como estas?
import asyncio
import websockets

async def procesar_mensaje(mensaje: str) -> str:
    m = mensaje.lower()
    if "hola matemático max" in m or "hola vicente" in m or "hola vicente max" in m:
        return "Estoy bien, gracias. ¿Y tú?"
    if m.strip() == "ping":
        return "pong"
    return "No entendí tu mensaje."

async def handler(websocket, path):
    async for mensaje in websocket:
        respuesta = await procesar_mensaje(mensaje)
        await websocket.send(respuesta)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("VicenteMax WebSocket server running on ws://0.0.0.0:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
