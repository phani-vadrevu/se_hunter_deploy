import subprocess
import os
import time

HOME = os.getenv("HOME")
LOGS_DIRECTORY = os.path.join(HOME, "se_hunter_logs") 
PRUNE_FREQUENCY = 1000

def fetch_container_ids():
    o = subprocess.check_output(
            ['docker', 'ps', '-f', 'status=exited', '-q', '--no-trunc'])
    return set(o.split())


def main():
    prune_time = 0
    if not os.path.exists(LOGS_DIRECTORY):
        os.makedirs(LOGS_DIRECTORY)

    tried_containers = set()

    while True:
        container_ids = fetch_container_ids()
        # container_ids = ['b70ebfdf6dcc']
        container_ids = container_ids.difference(tried_containers)
        print container_ids
        for container_id in container_ids:
            subprocess.call("docker cp %s:/root/log.txt ~/log.txt" %
                                    (container_id,), shell=True)
            with open(os.path.join(HOME, "log.txt")) as f:
                log_id = f.readline().strip()
            target_path = os.path.join(LOGS_DIRECTORY, "logs_%s.tar.gz" % (log_id,))
            subprocess.call("docker cp %s:/root/shipped_logs.tar.gz %s" %
                                    (container_id, target_path), shell=True)
            tried_containers.add(container_id)
            # break
        # break
        time.sleep(10)
        if time.time() - prune_time > PRUNE_FREQUENCY: 
            subprocess.call('docker system prune -f --filter "until=15m"', shell=True) 
            prune_time = time.time()



if __name__ == "__main__":
    main()
