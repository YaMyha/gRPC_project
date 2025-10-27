import grpc
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

class GreeterService(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message=f"Привет, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ Сервер запущен на порту 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
