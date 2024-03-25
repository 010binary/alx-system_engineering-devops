---
# Nginx Overview

## Introduction
Nginx is a powerful web server that also functions as a reverse proxy, load balancer, mail proxy, and HTTP cache. Developed by Russian developer Igor Sysoev and released in 2004, Nginx is free and open-source software distributed under the 2-clause BSD license.

## Popularity and Usage
Nginx is widely utilized, with a significant portion of web servers employing it, particularly as a load balancer. As of June 2022, Nginx ranked first among web servers, surpassing competitors like Apache and Cloudflare Server.

## Features
- Easy configuration for serving static web content or acting as a proxy server.
- Supports serving dynamic content using FastCGI, SCGI handlers, WSGI application servers, or Phusion Passenger modules.
- Utilizes an asynchronous event-driven approach, providing predictable performance under high loads.

## Nginx Plus
Nginx offers two versions: 
- **Nginx Open Source**: Free and open-source.
- **Nginx Plus**: A subscription-based model with additional features such as advanced load balancing, session persistence, DNS service discovery integration, and a web application firewall (WAF).

## Comparison with Apache
- Nginx was developed with the goal of outperforming the Apache web server.
- While Apache and Nginx offer similar performance since Apache 2.4, Nginx previously had a performance advantage but with decreased flexibility.
- Nginx has a modular architecture, and while adding third-party modules was initially cumbersome, dynamic module loading was introduced in version 1.9.11.

## History and Development
- Igor Sysoev began developing Nginx in 2002 to address the C10k problem and meet the needs of multiple websites, including the Rambler search engine and portal.
- Nginx Inc. was founded in 2011 to provide commercial products and support for Nginx.
- In March 2019, F5, Inc. acquired Nginx, Inc. for $670 million.
- Subsequent developments include the release of Nginx Unit in 2017 and the emergence of open-source forks such as Angie and freenginx.

---
