from UnionTools.PBFT.Node import Node
from UnionTools.Identity import Identity
from UnionTools.PBFT.PBFTRequest import Request, Pre_Prepare, Prepare, Commit, CheckPoint, ViewChange, Reply
import time


class PBFTSlaveNode(Node):
    def __init__(self, identity: Identity, client_ids) -> None:
        super().__init__(identity, client_ids)

    def request_stage(self, o, m, main_node):
        t = time.time()
        r_request = Request(t, o, self.identity.id, m)
        r_request.set_digest(self.sign_msg(m))
        msg_digest = self.sign_request(r_request)
        r_request.convert_into_dict()
        info = {'Package': r_request.param_dict, 'digest': msg_digest}
        res = self.send_msg(main_node, info, "/requestStage")
        return res

    def pre_prepare_stage(self, v, n, d, backup):
        pre_prepare_msg = Pre_Prepare(v, n, d)
        msg_digest = self.sign_msg(pre_prepare_msg)
        pre_prepare_msg.convert_into_dict()
        info = {'Package': pre_prepare_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(backup, info, "/prePrepareStage")
        return res

    def prepare_stage(self, v, n, d, i, main_node):
        prepare_msg = Prepare(v, n, d, i)
        msg_digest = self.sign_msg(prepare_msg)
        prepare_msg.convert_into_dict()
        info = {'Package': prepare_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(main_node, info, "/prepareStage")
        return res

    def commit_stage(self, v, n, d, i, main_node):
        commit_msg = Commit(v, n, d, i)
        msg_digest = self.sign_msg(commit_msg)
        commit_msg.convert_into_dict()
        info = {'Package': commit_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(main_node, info, "/commitStage")
        return res

    def reply_stage(self, v, c, i, r, main_node):
        reply_msg = Reply(v, c, i, r)
        msg_digest = self.sign_msg(reply_msg)
        reply_msg.convert_into_dict()
        info = {'Package': reply_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(main_node, info, "/replyStage")
        return res

    def checkpoint_stage(self, n, d, i,backup):
        check_point_msg = CheckPoint(n, d, i)
        msg_digest = self.sign_msg(check_point_msg)
        check_point_msg.convert_into_dict()
        info = {'Package': check_point_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(backup,info, "/checkpointStage")
        return res

    def view_change_stage(self, n, C, P, view,backup):
        view_change_msg = ViewChange(view, n, C, P, self.identity.id)
        msg_digest = self.sign_msg(view_change_msg)
        view_change_msg.convert_into_dict()
        info = {'Package': view_change_msg.param_dict, 'digest': msg_digest}
        res = self.send_msg(backup,info, "/viewChangeStage")
        return res

