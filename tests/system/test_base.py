from examplebeat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Examplebeat normally
        """
        self.render_config_template(
            path=os.path.abspath(self.working_dir) + "/log/*"
        )

        examplebeat_proc = self.start_beat()
        self.wait_until(lambda: self.log_contains("examplebeat is running"))
        exit_code = examplebeat_proc.kill_and_wait()
        assert exit_code == 0
