from digitalocean import Manager


class PolyManager(Manager):

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)

    def get_all_droplets(self, tag_name=None, page=1, per_page=200):
        """
            This function returns a list of Droplet object.
        """
        params = dict()
        if tag_name:
            params["tag_name"] = tag_name

        params["page"] = page
        params["per_page"] = per_page

        data = self.get_data("droplets/", params=params)

        return data

    def get_all_volumes(self, page=1, per_page=200):
        """
            This function returns a list of Volume objects.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page

        data = self.get_data("volumes/", params=params)

        return data

    def get_my_images(self, page=1, per_page=200):
        """
            This function returns a list of Image object.
        """
        params = {}
        params['private'] = 'true'
        params["page"] = page
        params["per_page"] = per_page

        data = self.get_data("images/", params=params)

        return data

    def get_all_load_balancers(self, page=1, per_page=200):
        """
            Returns a list of Load Balancer objects.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page
        data = self.get_data("load_balancers", params=params)

        return data

    def get_all_snapshots(self, page=1, per_page=200):
        """
            This method returns a list of all Snapshots.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page
        data = self.get_data("snapshots/", params=params)

        return data

    def get_all_firewalls(self, page=1, per_page=200):
        """
            This function returns a list of Firewall objects.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page
        data = self.get_data("firewalls", params=params)

        return data

    def get_all_cdns(self, page=1, per_page=200):
        """
            This function returns a list of Firewall objects.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page
        data = self.get_data("cdn/endpoints", params=params)

        return data

    def get_all_kubernetes(self, page=1, per_page=200):
        """
            This function returns a list of Firewall objects.
        """
        params = dict()
        params["page"] = page
        params["per_page"] = per_page
        data = self.get_data("kubernetes/clusters", params=params)

        return data
