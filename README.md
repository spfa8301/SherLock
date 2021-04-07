# “SherLock - Detecting Malicious Smartphone Behaviour ” 
## Cyber Security Network Analysis : MSBA
### Chidi Nzerem, Spencer Fairbairn, Tyler Tinker
#### Leeds School of Business

### Abstract:
##### The goal with this project is to be able to detect malicious behavior in smartphones. Cyber network security is a pillar of the project, as setting up a long term solution for looking into smartphone sensor data to detect malicious behavior would simplify the process by which users can see what specific data that their applications are taking without ever gaining root access to the devices involved. By allowing users to see what data is being collected on their smartphones they are able to take control of their own data through increased transparency between companies and users.

### BUSINESS UNDERSTANDING:
#### As personal computing power continues to become more accessible to the general public, smartphone usage has grown over 300% in the past 9 years hitting 3.2 billion users in 2019. Another astounding statistic that goes hand in hand with personal computing was that there were around 4 billion records breached in 2019. As smartphone usage increases we need systems to prevent malicious behaviour that applications set out to take or do to the users. By using the SherLock dataset created by “The BGU Cyber Security Research Center” we believe that we would be able to create a predictive model to allow us to know if an application is carrying out malicious behaviour. The primary purpose of the dataset is to help researchers and phone developers innovate means and methods of detecting malicious behavior in phones.  

### DATA UNDERSTANDING:
#### The dataset is organized into 8 data tables, one for each Sherlock probe. The sensors belonging to these probes return various records when sampled specifically the - wifi, bluetooth and local app sensors. Every table has the fields userid, uuid and version. The uuid stands for a unix millisecond timestamp of when a record was collected. The userid refers to the unique identifier for each user. Finally the version is the agents software release code.

