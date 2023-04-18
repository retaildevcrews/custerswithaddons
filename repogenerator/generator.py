"""Module providingFunction printing python version."""
import argparse
import os
import random
import shutil

def get_args():
    """Get and parse arguments for CLI"""
    ## Argument Parse
    parser = argparse.ArgumentParser(
        description="Generate git repo structure for testing"
    )
    parser.add_argument(
        "--cluster-group-count",
        default="1",
        required=True,
        help="Number of cluster groups to generate",
    )
    parser.add_argument(
        "--cluster-min-count",
        default=3,
        required=False,
        help="Min number of clusters per group",
    )
    parser.add_argument(
        "--cluster-max-count",
        default="10",
        required=False,
        help="Maximum number of clusters per group",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    cluster_group_count = int(args.cluster_group_count)
    cluster_min_count = int(args.cluster_min_count)
    cluster_max_count = int(args.cluster_max_count)
    print ("Cluster group count: " + str(cluster_group_count))
    print ("Cluster count max: " + str(cluster_max_count))
    print ("Cluster count min: " + str(cluster_min_count))
    for x in range(cluster_group_count):
        clustergroup_name='clustergroup-'+str(x)
        path='clustergroups/' + clustergroup_name
        os.makedirs(path)
        number_of_clusters=random.randrange(cluster_min_count,cluster_max_count)
        print('making: ' + str(number_of_clusters) + ' in clustergroup: ' + path)
        for y in range(number_of_clusters):
            apps_path=path+'/'+clustergroup_name+'-cluster-'+str(y)
            os.makedirs(apps_path)
            shutil.copytree('add-ons/apps', apps_path+'/apps')

                
