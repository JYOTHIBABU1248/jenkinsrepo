def test_mountfilesystem(storage_config,storage_client):
    partition = storage_config["server"]["device"]+"1"
    mntdir = storage_config["server"]["mount_point"]
    out = storage_client.mount_filesystem(mntdir,partition)
    verify = storage_client.ssh.runcmd(f"findmnt {mntdir}")
    assert mntdir in verify, f"mounting not happened"