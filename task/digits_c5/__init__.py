from .model import default_model
import flgo.benchmark.partition

default_model = default_model
default_partitioner = flgo.benchmark.partition.IIDPartitioner
default_partition_para = {'num_clients':100}
# visualize = flgo.benchmark.toolkits.visualization.visualize_by_class