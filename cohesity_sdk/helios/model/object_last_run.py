"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.helios.model_utils import (  # noqa: F401
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
    from cohesity_sdk.helios.model.object_last_run_all_of import ObjectLastRunAllOf
    from cohesity_sdk.helios.model.object_summary import ObjectSummary
    from cohesity_sdk.helios.model.object_type_v_center_params import ObjectTypeVCenterParams
    from cohesity_sdk.helios.model.sharepoint_object_params import SharepointObjectParams
    globals()['ObjectLastRunAllOf'] = ObjectLastRunAllOf
    globals()['ObjectSummary'] = ObjectSummary
    globals()['ObjectTypeVCenterParams'] = ObjectTypeVCenterParams
    globals()['SharepointObjectParams'] = SharepointObjectParams


class ObjectLastRun(ModelComposed):
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
        ('environment',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KAZURE': "kAzure",
            'KKVM': "kKVM",
            'KAWS': "kAWS",
            'KACROPOLIS': "kAcropolis",
            'KGCP': "kGCP",
            'KPHYSICAL': "kPhysical",
            'KPHYSICALFILES': "kPhysicalFiles",
            'KISILON': "kIsilon",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KFLASHBLADE': "kFlashBlade",
            'KELASTIFILE': "kElastifile",
            'KGPFS': "kGPFS",
            'KPURE': "kPure",
            'KNIMBLE': "kNimble",
            'KSQL': "kSQL",
            'KORACLE': "kOracle",
            'KEXCHANGE': "kExchange",
            'KAD': "kAD",
            'KVIEW': "kView",
            'KO365': "kO365",
            'KHYPERFLEX': "kHyperFlex",
            'KKUBERNETES': "kKubernetes",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
            'KSFDC': "kSfdc",
        },
        ('object_type',): {
            'None': None,
            'KCLUSTER': "kCluster",
            'KVSERVER': "kVserver",
            'KVOLUME': "kVolume",
            'KVCENTER': "kVCenter",
            'KSTANDALONEHOST': "kStandaloneHost",
            'KVCLOUDDIRECTOR': "kvCloudDirector",
            'KFOLDER': "kFolder",
            'KDATACENTER': "kDatacenter",
            'KCOMPUTERESOURCE': "kComputeResource",
            'KCLUSTERCOMPUTERESOURCE': "kClusterComputeResource",
            'KRESOURCEPOOL': "kResourcePool",
            'KDATASTORE': "kDatastore",
            'KHOSTSYSTEM': "kHostSystem",
            'KVIRTUALMACHINE': "kVirtualMachine",
            'KVIRTUALAPP': "kVirtualApp",
            'KSTORAGEPOD': "kStoragePod",
            'KNETWORK': "kNetwork",
            'KDISTRIBUTEDVIRTUALPORTGROUP': "kDistributedVirtualPortgroup",
            'KTAGCATEGORY': "kTagCategory",
            'KTAG': "kTag",
            'KOPAQUENETWORK': "kOpaqueNetwork",
            'KORGANIZATION': "kOrganization",
            'KVIRTUALDATACENTER': "kVirtualDatacenter",
            'KCATALOG': "kCatalog",
            'KORGMETADATA': "kOrgMetadata",
            'KSTORAGEPOLICY': "kStoragePolicy",
            'KVIRTUALAPPTEMPLATE': "kVirtualAppTemplate",
            'KDOMAIN': "kDomain",
            'KOUTLOOK': "kOutlook",
            'KMAILBOX': "kMailbox",
            'KUSERS': "kUsers",
            'KGROUPS': "kGroups",
            'KSITES': "kSites",
            'KUSER': "kUser",
            'KGROUP': "kGroup",
            'KSITE': "kSite",
            'KAPPLICATION': "kApplication",
            'KGRAPHUSER': "kGraphUser",
            'KPUBLICFOLDERS': "kPublicFolders",
            'KPUBLICFOLDER': "kPublicFolder",
            'KTEAMS': "kTeams",
            'KTEAM': "kTeam",
            'KKEYSPACE': "kKeyspace",
            'KTABLE': "kTable",
            'KDATABASE': "kDatabase",
            'KCOLLECTION': "kCollection",
            'KBUCKET': "kBucket",
            'KNAMESPACE': "kNamespace",
            'KSCVMMSERVER': "kSCVMMServer",
            'KSTANDALONECLUSTER': "kStandaloneCluster",
            'KHOSTGROUP': "kHostGroup",
            'KHYPERVHOST': "kHypervHost",
            'KHOSTCLUSTER': "kHostCluster",
            'KCUSTOMPROPERTY': "kCustomProperty",
            'KSUBSCRIPTION': "kSubscription",
            'KRESOURCEGROUP': "kResourceGroup",
            'KSTORAGEACCOUNT': "kStorageAccount",
            'KSTORAGEKEY': "kStorageKey",
            'KSTORAGECONTAINER': "kStorageContainer",
            'KSTORAGEBLOB': "kStorageBlob",
            'KNETWORKSECURITYGROUP': "kNetworkSecurityGroup",
            'KVIRTUALNETWORK': "kVirtualNetwork",
            'KSUBNET': "kSubnet",
            'KCOMPUTEOPTIONS': "kComputeOptions",
            'KSNAPSHOTMANAGERPERMIT': "kSnapshotManagerPermit",
            'KAVAILABILITYSET': "kAvailabilitySet",
            'KOVIRTMANAGER': "kOVirtManager",
            'KHOST': "kHost",
            'KSTORAGEDOMAIN': "kStorageDomain",
            'KVNICPROFILE': "kVNicProfile",
            'KIAMUSER': "kIAMUser",
            'KREGION': "kRegion",
            'KAVAILABILITYZONE': "kAvailabilityZone",
            'KEC2INSTANCE': "kEC2Instance",
            'KVPC': "kVPC",
            'KINSTANCETYPE': "kInstanceType",
            'KKEYPAIR': "kKeyPair",
            'KRDSOPTIONGROUP': "kRDSOptionGroup",
            'KRDSPARAMETERGROUP': "kRDSParameterGroup",
            'KRDSINSTANCE': "kRDSInstance",
            'KRDSSUBNET': "kRDSSubnet",
            'KRDSTAG': "kRDSTag",
            'KAURORATAG': "kAuroraTag",
            'KAURORACLUSTER': "kAuroraCluster",
            'KACCOUNT': "kAccount",
            'KSUBTASKPERMIT': "kSubTaskPermit",
            'KPROJECT': "kProject",
            'KLABEL': "kLabel",
            'KMETADATA': "kMetadata",
            'KVPCCONNECTOR': "kVPCConnector",
            'KPRISMCENTRAL': "kPrismCentral",
            'KOTHERHYPERVISORCLUSTER': "kOtherHypervisorCluster",
            'KDFSGROUP': "kDfsGroup",
            'KDFSTOPDIR': "kDfsTopDir",
            'KZONE': "kZone",
            'KMOUNTPOINT': "kMountPoint",
            'KSTORAGEARRAY': "kStorageArray",
            'KFILESYSTEM': "kFileSystem",
            'KCONTAINER': "kContainer",
            'KFILESYSTEM': "kFilesystem",
            'KFILESET': "kFileset",
            'KVIEWBOX': "kViewBox",
            'KVIEW': "kView",
            'KWINDOWSCLUSTER': "kWindowsCluster",
            'KORACLERACCLUSTER': "kOracleRACCluster",
            'KORACLEAPCLUSTER': "kOracleAPCluster",
            'KSERVICE': "kService",
            'KPVC': "kPVC",
            'KPERSISTENTVOLUMECLAIM': "kPersistentVolumeClaim",
            'KPERSISTENTVOLUME': "kPersistentVolume",
            'KROOTCONTAINER': "kRootContainer",
            'KDAGROOTCONTAINER': "kDAGRootContainer",
            'KEXCHANGENODE': "kExchangeNode",
            'KEXCHANGEDAGDATABASECOPY': "kExchangeDAGDatabaseCopy",
            'KEXCHANGESTANDALONEDATABASE': "kExchangeStandaloneDatabase",
            'KEXCHANGEDAG': "kExchangeDAG",
            'KEXCHANGEDAGDATABASE': "kExchangeDAGDatabase",
            'KDOMAINCONTROLLER': "kDomainController",
            'KINSTANCE': "kInstance",
            'KAAG': "kAAG",
            'KAAGROOTCONTAINER': "kAAGRootContainer",
            'KRACROOTCONTAINER': "kRACRootContainer",
            'KTABLESPACE': "kTableSpace",
            'KPDB': "kPDB",
            'KOBJECT': "kObject",
            'KORG': "kOrg",
            'KAPPINSTANCE': "kAppInstance",
        },
        ('protection_type',): {
            'None': None,
            'KAGENT': "kAgent",
            'KNATIVE': "kNative",
            'KSNAPSHOTMANAGER': "kSnapshotManager",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KFILE': "kFile",
            'KVOLUME': "kVolume",
        },
        ('os_type',): {
            'None': None,
            'KLINUX': "kLinux",
            'KWINDOWS': "kWindows",
            'KAIX': "kAix",
            'KSOLARIS': "kSolaris",
            'KSAPHANA': "kSapHana",
            'KOTHER': "kOther",
        },
        ('backup_run_status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
            'PAUSED': "Paused",
        },
        ('archival_run_status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
            'PAUSED': "Paused",
        },
        ('replication_run_status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
            'PAUSED': "Paused",
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
            'id': (int, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'source_name': (str, none_type,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'object_hash': (str, none_type,),  # noqa: E501
            'object_type': (str, none_type,),  # noqa: E501
            'logical_size_bytes': (int, none_type,),  # noqa: E501
            'uuid': (str, none_type,),  # noqa: E501
            'global_id': (str, none_type,),  # noqa: E501
            'protection_type': (str, none_type,),  # noqa: E501
            'os_type': (str, none_type,),  # noqa: E501
            'v_center_summary': (ObjectTypeVCenterParams,),  # noqa: E501
            'sharepoint_site_summary': (SharepointObjectParams,),  # noqa: E501
            'run_id': (str,),  # noqa: E501
            'protection_group_name': (str, none_type,),  # noqa: E501
            'protection_group_id': (str, none_type,),  # noqa: E501
            'policy_name': (str, none_type,),  # noqa: E501
            'policy_id': (str, none_type,),  # noqa: E501
            'backup_run_status': (str, none_type,),  # noqa: E501
            'archival_run_status': (str, none_type,),  # noqa: E501
            'replication_run_status': (str, none_type,),  # noqa: E501
            'is_sla_violated': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'source_name': 'sourceName',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'object_hash': 'objectHash',  # noqa: E501
        'object_type': 'objectType',  # noqa: E501
        'logical_size_bytes': 'logicalSizeBytes',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'global_id': 'globalId',  # noqa: E501
        'protection_type': 'protectionType',  # noqa: E501
        'os_type': 'osType',  # noqa: E501
        'v_center_summary': 'vCenterSummary',  # noqa: E501
        'sharepoint_site_summary': 'sharepointSiteSummary',  # noqa: E501
        'run_id': 'runId',  # noqa: E501
        'protection_group_name': 'protectionGroupName',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'policy_name': 'policyName',  # noqa: E501
        'policy_id': 'policyId',  # noqa: E501
        'backup_run_status': 'backupRunStatus',  # noqa: E501
        'archival_run_status': 'archivalRunStatus',  # noqa: E501
        'replication_run_status': 'replicationRunStatus',  # noqa: E501
        'is_sla_violated': 'isSlaViolated',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ObjectLastRun - a model defined in OpenAPI

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

            id (int, none_type): Specifies object id.. [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the object.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies registered source id to which object belongs.. [optional]  # noqa: E501
            source_name (str, none_type): Specifies registered source name to which object belongs.. [optional]  # noqa: E501
            environment (str, none_type): Specifies the environment of the object.. [optional]  # noqa: E501
            object_hash (str, none_type): Specifies the hash identifier of the object.. [optional]  # noqa: E501
            object_type (str, none_type): Specifies the type of the object.. [optional]  # noqa: E501
            logical_size_bytes (int, none_type): Specifies the logical size of object in bytes.. [optional]  # noqa: E501
            uuid (str, none_type): Specifies the uuid which is a unique identifier of the object.. [optional]  # noqa: E501
            global_id (str, none_type): Specifies the global id which is a unique identifier of the object.. [optional]  # noqa: E501
            protection_type (str, none_type): Specifies the protection type of the object if any.. [optional]  # noqa: E501
            os_type (str, none_type): Specifies the operating system type of the object.. [optional]  # noqa: E501
            v_center_summary (ObjectTypeVCenterParams): [optional]  # noqa: E501
            sharepoint_site_summary (SharepointObjectParams): [optional]  # noqa: E501
            run_id (str): Specifies the last run id.. [optional]  # noqa: E501
            protection_group_name (str, none_type): Specifies the protection group name of last run.. [optional]  # noqa: E501
            protection_group_id (str, none_type): Specifies the protection group id of last run.. [optional]  # noqa: E501
            policy_name (str, none_type): Specifies the policy name of last run.. [optional]  # noqa: E501
            policy_id (str, none_type): Specifies the policy id of last run.. [optional]  # noqa: E501
            backup_run_status (str, none_type): Specifies the status of last local back up run.. [optional]  # noqa: E501
            archival_run_status (str, none_type): Specifies the status of last archival run.. [optional]  # noqa: E501
            replication_run_status (str, none_type): Specifies the status of last replication run.. [optional]  # noqa: E501
            is_sla_violated (bool, none_type): Specifies if the sla is violated in last run.. [optional]  # noqa: E501
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


        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              ObjectLastRunAllOf,
              ObjectSummary,
          ],
          'oneOf': [
          ],
        }

