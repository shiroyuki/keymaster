from argparse import ArgumentParser, Namespace

from gallium import ICommand
from gallium.interface import alias

from keymaster.cli.kms.inline.abc import InlineError, InlineRuntimeError
from keymaster.cli.kms.inline.copy_password import CopyPassword
from keymaster.cli.kms.inline.get import Get
from keymaster.cli.kms.inline.search import Search


@alias('sh')
class InteractiveShell(ICommand):
    def identifier(self):
        return 'shell'

    def define(self, parser: ArgumentParser):
        pass

    def execute(self, args: Namespace):
        print('To list all commands, type "list".')
        print('To exit, please press CTRL+C or type "exit".\n')

        cmd_list = sorted(
            [
                Get(),
                Search(),
                CopyPassword(),
            ],
            key=lambda c: c.get_aliases()[0]
        )

        try:
            while True:
                response = self.ask('[keymaster]').strip()

                if response == 'exit':
                    break

                if response == 'list':
                    for cmd in cmd_list:
                        print(f' - {cmd.get_aliases()[0]}')

                    print('\nFor more information, please type the command with -h.\n')
                    continue

                split_response = response.split(' ', 1)

                if len(split_response) == 1:
                    cmd_name = split_response[0]
                    raw_args = None
                else:
                    cmd_name, raw_args = split_response

                target_cmd = None

                for cmd in cmd_list:
                    if cmd_name not in cmd.get_aliases():
                        continue
                    target_cmd = cmd

                if not target_cmd:
                    print('ERROR: Command not found')

                try:
                    args = target_cmd.get_parser().parse_args(raw_args.split(' '))
                except InlineError:
                    print('')
                    continue

                try:
                    target_cmd.run(args)
                except InlineRuntimeError as e:
                    print(f'ERROR: {e}')
                print('')

        except KeyboardInterrupt:
            pass
        finally:
            print('\nSee you later :D')
