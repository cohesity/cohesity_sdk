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
    from cohesity_sdk.cluster.model.archival_run import ArchivalRun
    from cohesity_sdk.cluster.model.backup_run import BackupRun
    from cohesity_sdk.cluster.model.cloud_spin_run import CloudSpinRun
    from cohesity_sdk.cluster.model.cluster_identifier import ClusterIdentifier
    from cohesity_sdk.cluster.model.on_prem_deploy_run import OnPremDeployRun
    from cohesity_sdk.cluster.model.replication_run import ReplicationRun
    from cohesity_sdk.cluster.model.tenant import Tenant
    globals()['ArchivalRun'] = ArchivalRun
    globals()['BackupRun'] = BackupRun
    globals()['CloudSpinRun'] = CloudSpinRun
    globals()['ClusterIdentifier'] = ClusterIdentifier
    globals()['OnPremDeployRun'] = OnPremDeployRun
    globals()['ReplicationRun'] = ReplicationRun
    globals()['Tenant'] = Tenant


class ObjectProtectionRunInfo(ModelNormal):
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
        ('data_lock',): {
            'None': None,
            'COMPLIANCE': "Compliance",
            'ADMINISTRATIVE': "Administrative",
        },
        ('run_type',): {
            'None': None,
            'KREGULAR': "kRegular",
            'KFULL': "kFull",
            'KLOG': "kLog",
            'KSYSTEM': "kSystem",
            'KHYDRATECDP': "kHydrateCDP",
            'KSTORAGEARRAYSNAPSHOT': "kStorageArraySnapshot",
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
            'archival_info': (ArchivalRun,),  # noqa: E501
            'cloud_spin_info': (CloudSpinRun,),  # noqa: E501
            'data_lock': (str, none_type,),  # noqa: E501
            'is_cloud_archival_direct': (bool, none_type,),  # noqa: E501
            'is_local_snapshots_deleted': (bool, none_type,),  # noqa: E501
            'is_replication_run': (bool, none_type,),  # noqa: E501
            'is_sla_violated': (bool, none_type,),  # noqa: E501
            'local_snapshot_info': (BackupRun,),  # noqa: E501
            'on_legal_hold': (bool, none_type,),  # noqa: E501
            'on_prem_deploy_info': (OnPremDeployRun,),  # noqa: E501
            'origin_cluster_identifier': (ClusterIdentifier,),  # noqa: E501
            'origin_protection_group_id': (str, none_type,),  # noqa: E501
            'original_backup_info': (BackupRun,),  # noqa: E501
            'permissions': ([Tenant], none_type,),  # noqa: E501
            'policy_id': (str, none_type,),  # noqa: E501
            'policy_name': (str, none_type,),  # noqa: E501
            'protection_group_id': (str, none_type,),  # noqa: E501
            'protection_group_name': (str, none_type,),  # noqa: E501
            'replication_info': (ReplicationRun,),  # noqa: E501
            'run_id': (str, none_type,),  # noqa: E501
            'run_label': (str, none_type,),  # noqa: E501
            'run_type': (str, none_type,),  # noqa: E501
            'storage_domain_id': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'archival_info': 'archivalInfo',  # noqa: E501
        'cloud_spin_info': 'cloudSpinInfo',  # noqa: E501
        'data_lock': 'dataLock',  # noqa: E501
        'is_cloud_archival_direct': 'isCloudArchivalDirect',  # noqa: E501
        'is_local_snapshots_deleted': 'isLocalSnapshotsDeleted',  # noqa: E501
        'is_replication_run': 'isReplicationRun',  # noqa: E501
        'is_sla_violated': 'isSlaViolated',  # noqa: E501
        'local_snapshot_info': 'localSnapshotInfo',  # noqa: E501
        'on_legal_hold': 'onLegalHold',  # noqa: E501
        'on_prem_deploy_info': 'onPremDeployInfo',  # noqa: E501
        'origin_cluster_identifier': 'originClusterIdentifier',  # noqa: E501
        'origin_protection_group_id': 'originProtectionGroupId',  # noqa: E501
        'original_backup_info': 'originalBackupInfo',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'policy_id': 'policyId',  # noqa: E501
        'policy_name': 'policyName',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'protection_group_name': 'protectionGroupName',  # noqa: E501
        'replication_info': 'replicationInfo',  # noqa: E501
        'run_id': 'runId',  # noqa: E501
        'run_label': 'runLabel',  # noqa: E501
        'run_type': 'runType',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
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
        """ObjectProtectionRunInfo - a model defined in OpenAPI

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

            archival_info (ArchivalRun): [optional]  # noqa: E501
            cloud_spin_info (CloudSpinRun): [optional]  # noqa: E501
            data_lock (str, none_type): Specifies WORM retention type for the local backeup. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept until the maximum of the snapshot retention time. During that time, the snapshots cannot be deleted. <br>'Compliance' implies WORM retention is set for compliance reason. <br>'Administrative' implies WORM retention is set for administrative purposes.. [optional]  # noqa: E501
            is_cloud_archival_direct (bool, none_type): Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location.. [optional]  # noqa: E501
            is_local_snapshots_deleted (bool, none_type): Specifies if snapshots for this run has been deleted.. [optional]  # noqa: E501
            is_replication_run (bool, none_type): Specifies if this protection run is a replication run.. [optional]  # noqa: E501
            is_sla_violated (bool, none_type): Indicated if SLA has been violated for this run.. [optional]  # noqa: E501
            local_snapshot_info (BackupRun): [optional]  # noqa: E501
            on_legal_hold (bool, none_type): Specifies if object's snapshot is on legal hold.. [optional]  # noqa: E501
            on_prem_deploy_info (OnPremDeployRun): [optional]  # noqa: E501
            origin_cluster_identifier (ClusterIdentifier): [optional]  # noqa: E501
            origin_protection_group_id (str, none_type): ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run.. [optional]  # noqa: E501
            original_backup_info (BackupRun): [optional]  # noqa: E501
            permissions ([Tenant], none_type): Specifies the list of tenants that have permissions for this protection group run.. [optional]  # noqa: E501
            policy_id (str, none_type): Specifies the unique id of the Protection Policy associated with the Protection Run. The Policy provides retry settings Protection Schedules, Priority, SLA, etc.. [optional]  # noqa: E501
            policy_name (str, none_type): Specifies Specifies the name of the Protection Policy.. [optional]  # noqa: E501
            protection_group_id (str, none_type): ProtectionGroupId to which this run belongs. This will only be populated if the object is protected by a protection group.. [optional]  # noqa: E501
            protection_group_name (str, none_type): Name of the Protection Group to which this run belongs. This will only be populated if the object is protected by a protection group.. [optional]  # noqa: E501
            replication_info (ReplicationRun): [optional]  # noqa: E501
            run_id (str, none_type): Specifies the ID of the protection run.. [optional]  # noqa: E501
            run_label (str, none_type): Specifies a label with which this run is created. Only applicable for user triggered protect now action.. [optional]  # noqa: E501
            run_type (str, none_type): Type of Protection run. 'kRegular' indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. 'kFull' indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. 'kLog' indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. 'kSystem' indicates system volume backup. It produces an image for bare metal recovery.. [optional]  # noqa: E501
            storage_domain_id (int, none_type): Specifies the Storage Domain (View Box) ID where this Protection Run writes data.. [optional]  # noqa: E501
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


