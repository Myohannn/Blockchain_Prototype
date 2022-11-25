# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_utils import blockchain_pb2 as grpc__utils_dot_blockchain__pb2


class BlockChainStub(object):
  """blockchain service and the function definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.initTxList = channel.unary_unary(
        '/BlockChain/initTxList',
        request_serializer=grpc__utils_dot_blockchain__pb2.InitTxListRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.InitTxListResponse.FromString,
        )
    self.addNewBlock = channel.unary_unary(
        '/BlockChain/addNewBlock',
        request_serializer=grpc__utils_dot_blockchain__pb2.AddBlockRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.AddBlockResponse.FromString,
        )
    self.QueryBlockchain = channel.unary_unary(
        '/BlockChain/QueryBlockchain',
        request_serializer=grpc__utils_dot_blockchain__pb2.QueryBlockchainRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.QueryBlockchainResponse.FromString,
        )
    self.QueryBlock = channel.unary_unary(
        '/BlockChain/QueryBlock',
        request_serializer=grpc__utils_dot_blockchain__pb2.QueryBlockRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.QueryBlockResponse.FromString,
        )
    self.receiveBlock = channel.unary_unary(
        '/BlockChain/receiveBlock',
        request_serializer=grpc__utils_dot_blockchain__pb2.ReceiveBlockRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.ReceiveBlockResponse.FromString,
        )
    self.receiveMessage = channel.unary_unary(
        '/BlockChain/receiveMessage',
        request_serializer=grpc__utils_dot_blockchain__pb2.receiveMessageRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.receiveMessageResponse.FromString,
        )
    self.getUTXOs = channel.unary_unary(
        '/BlockChain/getUTXOs',
        request_serializer=grpc__utils_dot_blockchain__pb2.getUTXOsRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.getUTXOsResponse.FromString,
        )
    self.getState = channel.unary_unary(
        '/BlockChain/getState',
        request_serializer=grpc__utils_dot_blockchain__pb2.getStateRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.getStateResponse.FromString,
        )
    self.getchain = channel.unary_unary(
        '/BlockChain/getchain',
        request_serializer=grpc__utils_dot_blockchain__pb2.getchainRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.getchainResponse.FromString,
        )
    self.sendTransaction = channel.unary_unary(
        '/BlockChain/sendTransaction',
        request_serializer=grpc__utils_dot_blockchain__pb2.sendTransactionRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.sendTransactionResponse.FromString,
        )
    self.addNewtransaction = channel.unary_unary(
        '/BlockChain/addNewtransaction',
        request_serializer=grpc__utils_dot_blockchain__pb2.addNewRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.addNewResponse.FromString,
        )
    self.QueryDB = channel.unary_unary(
        '/BlockChain/QueryDB',
        request_serializer=grpc__utils_dot_blockchain__pb2.QueryDBRequest.SerializeToString,
        response_deserializer=grpc__utils_dot_blockchain__pb2.QueryDBResponse.FromString,
        )


class BlockChainServicer(object):
  """blockchain service and the function definition
  """

  def initTxList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addNewBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryBlockchain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryBlock(self, request, context):
    """For step 3
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def receiveBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def receiveMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUTXOs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getchain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addNewtransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryDB(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlockChainServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'initTxList': grpc.unary_unary_rpc_method_handler(
          servicer.initTxList,
          request_deserializer=grpc__utils_dot_blockchain__pb2.InitTxListRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.InitTxListResponse.SerializeToString,
      ),
      'addNewBlock': grpc.unary_unary_rpc_method_handler(
          servicer.addNewBlock,
          request_deserializer=grpc__utils_dot_blockchain__pb2.AddBlockRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.AddBlockResponse.SerializeToString,
      ),
      'QueryBlockchain': grpc.unary_unary_rpc_method_handler(
          servicer.QueryBlockchain,
          request_deserializer=grpc__utils_dot_blockchain__pb2.QueryBlockchainRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.QueryBlockchainResponse.SerializeToString,
      ),
      'QueryBlock': grpc.unary_unary_rpc_method_handler(
          servicer.QueryBlock,
          request_deserializer=grpc__utils_dot_blockchain__pb2.QueryBlockRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.QueryBlockResponse.SerializeToString,
      ),
      'receiveBlock': grpc.unary_unary_rpc_method_handler(
          servicer.receiveBlock,
          request_deserializer=grpc__utils_dot_blockchain__pb2.ReceiveBlockRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.ReceiveBlockResponse.SerializeToString,
      ),
      'receiveMessage': grpc.unary_unary_rpc_method_handler(
          servicer.receiveMessage,
          request_deserializer=grpc__utils_dot_blockchain__pb2.receiveMessageRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.receiveMessageResponse.SerializeToString,
      ),
      'getUTXOs': grpc.unary_unary_rpc_method_handler(
          servicer.getUTXOs,
          request_deserializer=grpc__utils_dot_blockchain__pb2.getUTXOsRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.getUTXOsResponse.SerializeToString,
      ),
      'getState': grpc.unary_unary_rpc_method_handler(
          servicer.getState,
          request_deserializer=grpc__utils_dot_blockchain__pb2.getStateRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.getStateResponse.SerializeToString,
      ),
      'getchain': grpc.unary_unary_rpc_method_handler(
          servicer.getchain,
          request_deserializer=grpc__utils_dot_blockchain__pb2.getchainRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.getchainResponse.SerializeToString,
      ),
      'sendTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.sendTransaction,
          request_deserializer=grpc__utils_dot_blockchain__pb2.sendTransactionRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.sendTransactionResponse.SerializeToString,
      ),
      'addNewtransaction': grpc.unary_unary_rpc_method_handler(
          servicer.addNewtransaction,
          request_deserializer=grpc__utils_dot_blockchain__pb2.addNewRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.addNewResponse.SerializeToString,
      ),
      'QueryDB': grpc.unary_unary_rpc_method_handler(
          servicer.QueryDB,
          request_deserializer=grpc__utils_dot_blockchain__pb2.QueryDBRequest.FromString,
          response_serializer=grpc__utils_dot_blockchain__pb2.QueryDBResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'BlockChain', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))