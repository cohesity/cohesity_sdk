"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cluster.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from cohesity_sdk.cluster.model.capacity_by_tier import CapacityByTier
    from cohesity_sdk.cluster.model.chassis_info import ChassisInfo
    from cohesity_sdk.cluster.model.count_by_tier import CountByTier
    from cohesity_sdk.cluster.model.node_hardware_info import NodeHardwareInfo
    from cohesity_sdk.cluster.model.node_stats import NodeStats
    from cohesity_sdk.cluster.model.node_system_disk_info import NodeSystemDiskInfo
    globals()['CapacityByTier'] = CapacityByTier
    globals()['ChassisInfo'] = ChassisInfo
    globals()['CountByTier'] = CountByTier
    globals()['NodeHardwareInfo'] = NodeHardwareInfo
    globals()['NodeStats'] = NodeStats
    globals()['NodeSystemDiskInfo'] = NodeSystemDiskInfo


class Node(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {
        ('removal_reason',): {
            'None': None,
            'UNKNOWN': "Unknown",
            'AUTOHEALTHCHECK': "AutoHealthCheck",
            'USERGRACEFULREMOVAL': "UserGracefulRemoval",
            'USERAVOIDACCESS': "UserAvoidAccess",
            'USERGRACEFULNODEREMOVAL': "UserGracefulNodeRemoval",
            'USERREMOVEDOWNNODE': "UserRemoveDownNode",
            'BRIDGEDATAUNAVAILABLE': "BridgeDataUnavailable",
        },
        ('removal_state',): {
            'None': None,
            'DONTREMOVE': "DontRemove",
            'MARKEDFORREMOVAL': "MarkedForRemoval",
            'OKTOREMOVE': "OkToRemove",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'capacity_by_tier': ([CapacityByTier], none_type,),  # noqa: E501
            'chassis_info': (ChassisInfo,),  # noqa: E501
            'cluster_partition_id': (int, none_type,),  # noqa: E501
            'cluster_partition_name': (str, none_type,),  # noqa: E501
            'cohesity_node_serial': (str, none_type,),  # noqa: E501
            'disk_count_by_tier': ([CountByTier], none_type,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'ip': (str, none_type,),  # noqa: E501
            'is_app_node': (bool, none_type,),  # noqa: E501
            'is_marked_for_removal': (bool, none_type,),  # noqa: E501
            'max_physical_capacity_bytes': (int, none_type,),  # noqa: E501
            'node_hardware_info': (NodeHardwareInfo,),  # noqa: E501
            'node_incarnation_id': (int, none_type,),  # noqa: E501
            'node_software_version': (str, none_type,),  # noqa: E501
            'node_type': (str, none_type,),  # noqa: E501
            'offline_disk_count': (int, none_type,),  # noqa: E501
            'offline_mount_paths_of_disks': ([str], none_type,),  # noqa: E501
            'product_model': (str, none_type,),  # noqa: E501
            'vendor': (str, none_type,),  # noqa: E501
            'removal_reason': ([str], none_type,),  # noqa: E501
            'removal_state': (str, none_type,),  # noqa: E501
            'slot_number': (int, none_type,),  # noqa: E501
            'stats': (NodeStats,),  # noqa: E501
            'system_disks': ([NodeSystemDiskInfo], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'capacity_by_tier': 'capacityByTier',  # noqa: E501
        'chassis_info': 'chassisInfo',  # noqa: E501
        'cluster_partition_id': 'clusterPartitionId',  # noqa: E501
        'cluster_partition_name': 'clusterPartitionName',  # noqa: E501
        'cohesity_node_serial': 'cohesityNodeSerial',  # noqa: E501
        'disk_count_by_tier': 'diskCountByTier',  # noqa: E501
        'id': 'id',  # noqa: E501
        'ip': 'ip',  # noqa: E501
        'is_app_node': 'isAppNode',  # noqa: E501
        'is_marked_for_removal': 'isMarkedForRemoval',  # noqa: E501
        'max_physical_capacity_bytes': 'maxPhysicalCapacityBytes',  # noqa: E501
        'node_hardware_info': 'nodeHardwareInfo',  # noqa: E501
        'node_incarnation_id': 'nodeIncarnationId',  # noqa: E501
        'node_software_version': 'nodeSoftwareVersion',  # noqa: E501
        'node_type': 'nodeType',  # noqa: E501
        'offline_disk_count': 'offlineDiskCount',  # noqa: E501
        'offline_mount_paths_of_disks': 'offlineMountPathsOfDisks',  # noqa: E501
        'product_model': 'productModel',  # noqa: E501
        'vendor': 'vendor',  # noqa: E501
        'removal_reason': 'removalReason',  # noqa: E501
        'removal_state': 'removalState',  # noqa: E501
        'slot_number': 'slotNumber',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'system_disks': 'systemDisks',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Node - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)

            capacity_by_tier ([CapacityByTier], none_type): CapacityByTier describes the capacity of each storage tier.. [optional]  # noqa: E501
            chassis_info (ChassisInfo): [optional]  # noqa: E501
            cluster_partition_id (int, none_type): ClusterPartitionId is the Id of the cluster partition to which the Node belongs.. [optional]  # noqa: E501
            cluster_partition_name (str, none_type): ClusterPartitionName is the name of the cluster to which the Node belongs.. [optional]  # noqa: E501
            cohesity_node_serial (str, none_type): Cohesity Node Serial Number of the Node.. [optional]  # noqa: E501
            disk_count_by_tier ([CountByTier], none_type): DiskCountByTier describes the disk number of each storage tier.. [optional]  # noqa: E501
            id (int, none_type): Id is the Id of the Node.. [optional]  # noqa: E501
            ip (str, none_type): Ip is the IP address of the Node.. [optional]  # noqa: E501
            is_app_node (bool, none_type): Whether node is app node.. [optional]  # noqa: E501
            is_marked_for_removal (bool, none_type): IsMarkedForRemoval specifies whether the node has been marked for removal.. [optional]  # noqa: E501
            max_physical_capacity_bytes (int, none_type): MaxPhysicalCapacityBytes specifies the maximum physical capacity of the node in bytes.. [optional]  # noqa: E501
            node_hardware_info (NodeHardwareInfo): [optional]  # noqa: E501
            node_incarnation_id (int, none_type): NodeIncarnationId is the incarnation id  of this node. The incarnation id is changed every time the data is wiped from the node. Various services on a node is only run if incarnation id of the node matches the incarnation id of the cluster. Whenever a mismatch is detected, Nexus will stop all services and clean the data from the node. After clean operation is completed, Nexus will set the node incarnation id to cluster incarnation id and start the services.. [optional]  # noqa: E501
            node_software_version (str, none_type): NodeSoftwareVersion is the current version of Cohesity software installed on a node.. [optional]  # noqa: E501
            node_type (str, none_type): Node type: StorageNode, AllFlashNode, RoboNode, AppNode, etc.. [optional]  # noqa: E501
            offline_disk_count (int, none_type): OfflineDiskCount is the number of offline disks in a node.. [optional]  # noqa: E501
            offline_mount_paths_of_disks ([str], none_type): OfflineMountPathsOfDisks provides the corresponding mount paths for direct attached disks that are currently offline - access to these were detected to hang sometime in the past. After these disks have been fixed, their mount paths needs to be removed from the following list before these will be accessed again.. [optional]  # noqa: E501
            product_model (str, none_type): Specifies the product model of the node.. [optional]  # noqa: E501
            vendor (str, none_type): Specifies the vendor model of the node. [optional]  # noqa: E501
            removal_reason ([str], none_type): RemovalReason specifies the removal reason of the node. 'kAutoHealthCheck' means the entity health is bad. 'kUserGracefulRemoval' means user initiated a graceful removal. 'kUserAvoidAccess' means user initiated a mark offline. 'kUserGracefulNodeRemoval' mean users initiated graceful node removal. 'kUserRemoveDownNode' mean user initiated graceful removal of down node. 'kBridgeDataUnavailable' Bridge requested a graceful removal of a disk when it is not available.. [optional]  # noqa: E501
            removal_state (str, none_type): RemovalState specifies the removal state of the node. 'kDontRemove' means the state of object is functional and it is not being removed. 'kMarkedForRemoval' means the object is being removed. 'kOkToRemove' means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster.. [optional]  # noqa: E501
            slot_number (int, none_type): Slot number occupied by this node within the chassis.. [optional]  # noqa: E501
            stats (NodeStats): [optional]  # noqa: E501
            system_disks ([NodeSystemDiskInfo], none_type): SystemDisk describes the node system disks.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)


        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

