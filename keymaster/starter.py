from gallium.starter import main


def activate():
    main(
        console_name='keymaster' if __name__ == '__main__' else None,
        config_content=dict(imports=[
            'keymaster.client.cli.console',
            'keymaster.client.cli.generate_password',
            'keymaster.client.cli.import_lastpass',
            'keymaster.client.cli.login',
            'keymaster.server.cli.grpc_server_run',
            'keymaster.server.cli.setup',
        ]),
        in_isolation=True,
    )
