from credmark.cmf.model import Model
from credmark.dto import DTO, DTOField


class EchoDto(DTO):
    message: str = DTOField('Hello', description='A message')


@Model.describe(slug='example.echo',
                version='1.0',
                display_name='Echo',
                description="A test model to echo the message property sent in input.",
                developer='Credmark',
                input=EchoDto,
                output=EchoDto)
class EchoModel(Model):
    """
    This test simply echos back the input.
    The DTO message field defines a default value so that is
    used if no input is sent.
    """

    def run(self, input: EchoDto) -> EchoDto:
        return input
