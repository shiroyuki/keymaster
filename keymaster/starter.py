from gallium.starter import main


def activate():
    main(
        console_name='keymaster' if __name__ == '__main__' else None,
        config_content=dict(imports=[
            'keymaster.cli.kms.console',
            'keymaster.cli.util.import_lastpass',
        ]),
        in_isolation=True,
    )
