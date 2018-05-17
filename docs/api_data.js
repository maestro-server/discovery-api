define({ "api": [
  {
    "type": "get",
    "url": "/crawler/",
    "title": "3. Endpoints allowed",
    "name": "GetCrawler",
    "group": "Crawler",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"resources\": {\n        \"path\": (string)\n    }\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controller/crawler.py",
    "groupTitle": "Crawler"
  },
  {
    "type": "get",
    "url": "/crawler/<datacenter>",
    "title": "4. Resources allowed by provider",
    "name": "GetCrawlerDC",
    "group": "Crawler",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"resource\": (object) {\n        \"<api name>\": (string)\n    }\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controller/crawlerDcs.py",
    "groupTitle": "Crawler"
  },
  {
    "type": "get",
    "url": "/crawler/<datacenter>/<instance>/<task>",
    "title": "1. Health check",
    "name": "GetCrawlerInstance",
    "group": "Crawler",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    'datacenter': <string>,\n    'instance': <string>,\n    'task': <string>\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controller/crawlerApp.py",
    "groupTitle": "Crawler"
  },
  {
    "type": "put",
    "url": "/crawler/<datacenter>/<instance>/<task>",
    "title": "2. Execute crawler",
    "name": "PostDatacenterCrawler",
    "group": "Crawler",
    "description": "<p>Used to run jobs, all jobs execute in workers tasks. All task is process by discovery-worker</p>",
    "parameter": {
      "fields": {
        "Query": [
          {
            "group": "Query",
            "type": "String",
            "optional": false,
            "field": "instance",
            "description": "<p>Instance ID of connection.</p>"
          },
          {
            "group": "Query",
            "type": "String",
            "optional": false,
            "field": "task",
            "description": "<p>Task (server-list, db-list)</p>"
          },
          {
            "group": "Query",
            "type": "String",
            "optional": false,
            "field": "datacenter",
            "description": "<p>Datacenter name (AWS, OpenStack)</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n[{\n    'name': (string)\n}]",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controller/crawlerApp.py",
    "groupTitle": "Crawler"
  },
  {
    "type": "get",
    "url": "/",
    "title": "Ping",
    "name": "GetPing",
    "group": "Ping",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 201 OK\n{\n   app: (String)\n   description: (String)\n   version: (String)\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controller/home.py",
    "groupTitle": "Ping"
  }
] });