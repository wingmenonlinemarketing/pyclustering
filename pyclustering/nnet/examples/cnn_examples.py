"""!

@brief Examples of usage and demonstration of abilities of chaotic oscillatory network.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2020
@copyright BSD-3-Clause

"""

from pyclustering.nnet.cnn import cnn_network, cnn_visualizer, type_conn;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

from pyclustering.utils import read_sample;


def template_dynamic_cnn(num_osc, steps, stimulus, neighbors, connection, show_network = False):
    network_instance = cnn_network(num_osc, connection, amount_neighbors = neighbors);
    
    output_dynamic = network_instance.simulate(steps, stimulus);
    print(output_dynamic.allocate_sync_ensembles(10));
    
    if (show_network is True):
        network_instance.show_network();
    
    cnn_visualizer.show_output_dynamic(output_dynamic);
    cnn_visualizer.show_dynamic_matrix(output_dynamic);
    cnn_visualizer.show_observation_matrix(output_dynamic);


def chaotic_clustering_sample_simple_01():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    template_dynamic_cnn(len(sample), 100, sample, 3, type_conn.ALL_TO_ALL);


def chaotic_clustering_triangulation_sample_simple_01():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    template_dynamic_cnn(len(sample), 100, sample, 3, type_conn.TRIANGULATION_DELAUNAY);


def chaotic_clustering_sample_simple_02():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    template_dynamic_cnn(len(sample), 100, sample, 3, type_conn.ALL_TO_ALL);


def chaotic_clustering_triangulation_sample_simple_02():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    template_dynamic_cnn(len(sample), 100, sample, 5, type_conn.TRIANGULATION_DELAUNAY);


def chaotic_clustering_sample_simple_03():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE3);
    template_dynamic_cnn(len(sample), 100, sample, 10, type_conn.ALL_TO_ALL);


def chaotic_clustering_sample_simple_04():
    sample = read_sample(SIMPLE_SAMPLES.SAMPLE_SIMPLE4);
    template_dynamic_cnn(len(sample), 100, sample, 5, type_conn.ALL_TO_ALL);


def chaotic_clustering_fcps_lsun():
    sample = read_sample(FCPS_SAMPLES.SAMPLE_LSUN);
    template_dynamic_cnn(len(sample), 100, sample, 10, type_conn.ALL_TO_ALL);


chaotic_clustering_sample_simple_01();
chaotic_clustering_triangulation_sample_simple_01();
chaotic_clustering_sample_simple_02();
chaotic_clustering_triangulation_sample_simple_02();
chaotic_clustering_sample_simple_03();
chaotic_clustering_sample_simple_04();

chaotic_clustering_fcps_lsun();

