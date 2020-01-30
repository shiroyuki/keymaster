from gallium.starter import main

main(
    console_name='keymaster' if __name__ == '__main__' else None,
    config_content=dict(imports=[
        'keymaster.cli.kms.core_init',
        'keymaster.cli.kms.helper_lp_import',
    ]),
    in_isolation=True,
)
