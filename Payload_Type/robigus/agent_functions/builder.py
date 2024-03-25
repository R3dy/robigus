from mythic_container.PayloadBuilder import *
from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *

class Robigus(Payloadtype):
    name = "robigus"
    file_extension = "exe" # but this will probably be ELF 
    supported_os = [SupportedOS.Linux]
    wrapper = False
    wrapped_payloads = []
    note = "A Rust agent to hax boxes"
    supports_dynamic_loading = False
    mythic_encrypts = True
    build_parameters = [
            BuildParameter(
                name="architecture",
                parameter_type=BuildParameterType.ChooseOne,
                description="Choose your agent architecture ",
                choices=["AMD_x64", "ARM_x64"],
                default_value="AMD_x64",
                ),
            ]
    agent_path = pathlib.Path(".") / "agent_functions"
    agent_code_path = pathlib.Path(".") / "agent_code"
    c2_profiles = ["http"]
    translation_container = None

    async def build(self) -> BuildResponse:
        resp = BuildResponse(status=BuildStatus.Success)
        return resp
