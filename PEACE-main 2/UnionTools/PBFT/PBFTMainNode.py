from UnionTools.PBFT.Node import Node
from UnionTools.Identity import Identity
from UnionTools.PBFT.PBFTRequest import Request, Pre_Prepare, Prepare, Commit, CheckPoint, ViewChange, Reply
import time


class PBFTMainNode(Node):
    def __init__(self, identity: Identity, client_ids) -> None:
        super().__init__(identity, client_ids)

    def pre_prepare(self, info):
        r_request = Request.clean_init()
        self.resolve_info(r_request, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(r_request.client_id)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("客户端签名不正确")

        pre_prepare_reqeust = Pre_Prepare()

    def prepare(self, info):
        pre_prepare = Pre_Prepare.clean_init()
        self.resolve_info(pre_prepare, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(pre_prepare.client_id)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("预备请求签名不正确")

    def commit(self, info):
        prepare = Commit.clean_init()
        self.resolve_info(prepare, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(prepare.client_id)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("节点签名不正确")

    def view_change(self, info):
        view_change_req = ViewChange.clean_init()
        self.resolve_info(view_change_req, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(view_change_req.i)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("签名验证不通过")

    def reply(self, info):
        reply_request = Reply.clean_init()
        self.resolve_info(reply_request, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(reply_request.c)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("客户端签名不正确")

    def checkpoint(self, info):
        check_point_msg = CheckPoint.clean_init()
        self.resolve_info(check_point_msg, info['Package'])
        msg_digest = info['msg_digest']
        vk = self.pubkey_dict[str(check_point_msg.i)]

        if vk.verify(msg_digest, info['Package']) is False:
            raise Exception("签名不正确")