import sqlite3
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram(name="Advanced Web Service with On-Premise (colored)", show=False):
    ingress = Nginx("the INTERNET (ingress")

    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("warehouse 1"):
        grpcsvc = [
            Server("operatiuons room"),
            Server("router 2 grpc2"),
            Server("router 3 grpc3")]

    with Cluster("Sessions Cluster"):
        primary = Redis("session")
        primary - Edge(color="brown", style="dashed") - Redis("replica") << Edge(label="collect") << metrics
        grpcsvc >> Edge(color="brown") >> primary

    with Cluster("Service Desk Database"):
        primary = PostgreSQL("users")
        primary - Edge(color="brown", style="dotted") - PostgreSQL("replica") << Edge(label="collect") << metrics
        grpcsvc >> Edge(color="black") >> primary

    aggregator = Fluentd("logging")
    aggregator >> Edge(label="parse") >> Kafka("stream") >> Edge(color="black", style="bold") >> Spark("analytics")

    ingress >> Edge(color="darkgreen") << grpcsvc >> Edge(color="darkorange") >> aggregator
    
    
    Assumptions: 
        
        Search on premise data center, operations center architecture diagram active directory domain
        
        1 Operations center
    
         Ops Center, Finance, Accounting, IT, App Support,
    
    AD -> AWS connector for cloud integration and MFA
        
        1 warehouse/HUB inventory storage
          tracking mechanisms for the stuff. rfid/QRF/ gun, stuff. Also inventory system universal across platform
           internal AD network.
           
           Some switches for permanant areas/ whatever automation, physical automation, distribution equipment. These
           Also Wifi and extenders.
           
           Guest network, restricted, password or something. These
                 
          
          On prem Stuff:
              
         dev, qa, AD. biz specific, custom home grown. For
         
         Servicedesk/Helpdesk functions, call center, what vendor, cisco phones, mitel/ what the fuck is the name of it?
                  
         
          
          Cloud stuff: Connector to vendors API, have API to interface with vendor requests. 
    
    
     Future stuff, Zero Authentication, no vpn, no anything. These
     
     on prem databases, MS SQL, backups, transactional delta, full, or time period defined/ or size, 
     
     then used for analytics and metrics of inventory, Reporting database, or cubes.TimeoutError
     Analytics of data, capture of warehouse, meta data info, could use trends for analysis and forecasting for a CRM
     
     Common CRM for medical supplies? is there one? The
     
     
     Alerting and automation of process, both business and technology. triggers based on thresholds
     
     
     
    
    