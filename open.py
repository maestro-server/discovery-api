import openstack


def create_connection(auth_url, region, project_name, username, password):
    return openstack.connection.Connection(
        region_name=region,
        auth=dict(
            auth_url=auth_url,
            username='admin',
            password="secret",
            project_id=project_name,
            user_domain_id='default'
        ),
        compute_api_version='2'
    )


def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)


conn = create_connection("http://192.168.20.20/identity", "RegionOne", "44db5ee5699d419f82252e1812826d41", "admin",
                         "secret")
list_servers(conn)
