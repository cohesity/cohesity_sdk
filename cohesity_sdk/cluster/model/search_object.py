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
    from cohesity_sdk.cluster.model.object import Object
    from cohesity_sdk.cluster.model.object_protection_info import ObjectProtectionInfo
    from cohesity_sdk.cluster.model.object_protection_stats_summary import ObjectProtectionStatsSummary
    from cohesity_sdk.cluster.model.object_summary import ObjectSummary
    from cohesity_sdk.cluster.model.object_type_v_center_params import ObjectTypeVCenterParams
    from cohesity_sdk.cluster.model.object_type_windows_cluster_params import ObjectTypeWindowsClusterParams
    from cohesity_sdk.cluster.model.permission_info import PermissionInfo
    from cohesity_sdk.cluster.model.search_object_all_of import SearchObjectAllOf
    from cohesity_sdk.cluster.model.sharepoint_object_params import SharepointObjectParams
    from cohesity_sdk.cluster.model.snapshot_tag_info import SnapshotTagInfo
    from cohesity_sdk.cluster.model.tag_info import TagInfo
    from cohesity_sdk.cluster.model.tag_object import TagObject
    from cohesity_sdk.cluster.model.vmware_object_entity_params import VmwareObjectEntityParams
    globals()['Object'] = Object
    globals()['ObjectProtectionInfo'] = ObjectProtectionInfo
    globals()['ObjectProtectionStatsSummary'] = ObjectProtectionStatsSummary
    globals()['ObjectSummary'] = ObjectSummary
    globals()['ObjectTypeVCenterParams'] = ObjectTypeVCenterParams
    globals()['ObjectTypeWindowsClusterParams'] = ObjectTypeWindowsClusterParams
    globals()['PermissionInfo'] = PermissionInfo
    globals()['SearchObjectAllOf'] = SearchObjectAllOf
    globals()['SharepointObjectParams'] = SharepointObjectParams
    globals()['SnapshotTagInfo'] = SnapshotTagInfo
    globals()['TagInfo'] = TagInfo
    globals()['TagObject'] = TagObject
    globals()['VmwareObjectEntityParams'] = VmwareObjectEntityParams


class SearchObject(ModelComposed):
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
            'KAZURESQL': "kAzureSQL",
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
            'KIBMFLASHSYSTEM': "kIbmFlashSystem",
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
            'KROOTPUBLICFOLDER': "kRootPublicFolder",
            'KO365EXCHANGE': "kO365Exchange",
            'KO365ONEDRIVE': "kO365OneDrive",
            'KO365SHAREPOINT': "kO365Sharepoint",
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
            'KTENANT': "kTenant",
            'KSUBSCRIPTION': "kSubscription",
            'KRESOURCEGROUP': "kResourceGroup",
            'KSTORAGEACCOUNT': "kStorageAccount",
            'KSTORAGEKEY': "kStorageKey",
            'KSTORAGECONTAINER': "kStorageContainer",
            'KSTORAGEBLOB': "kStorageBlob",
            'KAPPLICATIONSECURITYGROUP': "kApplicationSecurityGroup",
            'KNETWORKSECURITYGROUP': "kNetworkSecurityGroup",
            'KVIRTUALNETWORK': "kVirtualNetwork",
            'KSUBNET': "kSubnet",
            'KCOMPUTEOPTIONS': "kComputeOptions",
            'KSNAPSHOTMANAGERPERMIT': "kSnapshotManagerPermit",
            'KAVAILABILITYSET': "kAvailabilitySet",
            'KSQLSERVER': "kSQLServer",
            'KSQLDATABASE': "kSQLDatabase",
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
            'KS3BUCKET': "kS3Bucket",
            'KS3TAG': "kS3Tag",
            'KKMSKEY': "kKmsKey",
            'KRDSPOSTGRESDB': "kRDSPostgresDb",
            'KAURORACLUSTERPOSTGRESDB': "kAuroraClusterPostgresDb",
            'KPROJECT': "kProject",
            'KLABEL': "kLabel",
            'KMETADATA': "kMetadata",
            'KVPCCONNECTOR': "kVPCConnector",
            'KPRISMCENTRAL': "kPrismCentral",
            'KOTHERHYPERVISORCLUSTER': "kOtherHypervisorCluster",
            'KZONE': "kZone",
            'KMOUNTPOINT': "kMountPoint",
            'KSTORAGEARRAY': "kStorageArray",
            'KFILESYSTEM': "kFileSystem",
            'KCONTAINER': "kContainer",
            'KFILESYSTEM': "kFilesystem",
            'KFILESET': "kFileset",
            'KPUREPROTECTIONGROUP': "kPureProtectionGroup",
            'KVOLUMEGROUP': "kVolumeGroup",
            'KSTORAGEPOOL': "kStoragePool",
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
            'KAAGDATABASE': "kAAGDatabase",
            'KRACROOTCONTAINER': "kRACRootContainer",
            'KTABLESPACE': "kTableSpace",
            'KPDB': "kPDB",
            'KOBJECT': "kObject",
            'KORG': "kOrg",
            'KAPPINSTANCE': "kAppInstance",
        },
        ('os_type',): {
            'None': None,
            'KLINUX': "kLinux",
            'KWINDOWS': "kWindows",
            'KAIX': "kAix",
            'KSOLARIS': "kSolaris",
            'KSAPHANA': "kSapHana",
            'KOTHER': "kOther",
            'KHPUX': "kHPUX",
            'KVOS': "kVOS",
        },
        ('protection_type',): {
            'None': None,
            'KAGENT': "kAgent",
            'KNATIVE': "kNative",
            'KSNAPSHOTMANAGER': "kSnapshotManager",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KAWSS3': "kAwsS3",
            'KAWSRDSPOSTGRESBACKUP': "kAwsRDSPostgresBackup",
            'KAZURESQL': "kAzureSQL",
            'KFILE': "kFile",
            'KVOLUME': "kVolume",
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
            'environment': (str, none_type,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'source_name': (str, none_type,),  # noqa: E501
            'child_objects': ([ObjectSummary], none_type,),  # noqa: E501
            'global_id': (str, none_type,),  # noqa: E501
            'logical_size_bytes': (int, none_type,),  # noqa: E501
            'object_hash': (str, none_type,),  # noqa: E501
            'object_type': (str, none_type,),  # noqa: E501
            'os_type': (str, none_type,),  # noqa: E501
            'protection_type': (str, none_type,),  # noqa: E501
            'sharepoint_site_summary': (SharepointObjectParams,),  # noqa: E501
            'uuid': (str, none_type,),  # noqa: E501
            'v_center_summary': (ObjectTypeVCenterParams,),  # noqa: E501
            'windows_cluster_summary': (ObjectTypeWindowsClusterParams,),  # noqa: E501
            'permissions': (PermissionInfo,),  # noqa: E501
            'protection_stats': ([ObjectProtectionStatsSummary], none_type,),  # noqa: E501
            'elastifile_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'flashblade_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'generic_nas_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'gpfs_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'group_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'isilon_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'mssql_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'netapp_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'oracle_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'physical_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'sharepoint_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'uda_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'view_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'vmware_params': (VmwareObjectEntityParams,),  # noqa: E501
            'snapshot_tags': ([SnapshotTagInfo], none_type,),  # noqa: E501
            'tags': ([TagInfo], none_type,),  # noqa: E501
            'object_protection_infos': ([ObjectProtectionInfo], none_type,),  # noqa: E501
            'source_info': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'environment': 'environment',  # noqa: E501
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'source_name': 'sourceName',  # noqa: E501
        'child_objects': 'childObjects',  # noqa: E501
        'global_id': 'globalId',  # noqa: E501
        'logical_size_bytes': 'logicalSizeBytes',  # noqa: E501
        'object_hash': 'objectHash',  # noqa: E501
        'object_type': 'objectType',  # noqa: E501
        'os_type': 'osType',  # noqa: E501
        'protection_type': 'protectionType',  # noqa: E501
        'sharepoint_site_summary': 'sharepointSiteSummary',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'v_center_summary': 'vCenterSummary',  # noqa: E501
        'windows_cluster_summary': 'windowsClusterSummary',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'protection_stats': 'protectionStats',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'group_params': 'groupParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'mssql_params': 'mssqlParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'oracle_params': 'oracleParams',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'sharepoint_params': 'sharepointParams',  # noqa: E501
        'uda_params': 'udaParams',  # noqa: E501
        'view_params': 'viewParams',  # noqa: E501
        'vmware_params': 'vmwareParams',  # noqa: E501
        'snapshot_tags': 'snapshotTags',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'object_protection_infos': 'objectProtectionInfos',  # noqa: E501
        'source_info': 'sourceInfo',  # noqa: E501
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
        """SearchObject - a model defined in OpenAPI

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

            environment (str, none_type): Specifies the environment of the object.. [optional]  # noqa: E501
            id (int, none_type): Specifies object id.. [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the object.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies registered source id to which object belongs.. [optional]  # noqa: E501
            source_name (str, none_type): Specifies registered source name to which object belongs.. [optional]  # noqa: E501
            child_objects ([ObjectSummary], none_type): Specifies child object details.. [optional]  # noqa: E501
            global_id (str, none_type): Specifies the global id which is a unique identifier of the object.. [optional]  # noqa: E501
            logical_size_bytes (int, none_type): Specifies the logical size of object in bytes.. [optional]  # noqa: E501
            object_hash (str, none_type): Specifies the hash identifier of the object.. [optional]  # noqa: E501
            object_type (str, none_type): Specifies the type of the object.. [optional]  # noqa: E501
            os_type (str, none_type): Specifies the operating system type of the object.. [optional]  # noqa: E501
            protection_type (str, none_type): Specifies the protection type of the object if any.. [optional]  # noqa: E501
            sharepoint_site_summary (SharepointObjectParams): [optional]  # noqa: E501
            uuid (str, none_type): Specifies the uuid which is a unique identifier of the object.. [optional]  # noqa: E501
            v_center_summary (ObjectTypeVCenterParams): [optional]  # noqa: E501
            windows_cluster_summary (ObjectTypeWindowsClusterParams): [optional]  # noqa: E501
            permissions (PermissionInfo): [optional]  # noqa: E501
            protection_stats ([ObjectProtectionStatsSummary], none_type): Specifies the count and size of protected and unprotected objects for the size.. [optional]  # noqa: E501
            elastifile_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Elastifile object.. [optional]  # noqa: E501
            flashblade_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Flashblade object.. [optional]  # noqa: E501
            generic_nas_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for GenericNas object.. [optional]  # noqa: E501
            gpfs_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for GPFS object.. [optional]  # noqa: E501
            group_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for M365 Group object.. [optional]  # noqa: E501
            isilon_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Isilon object.. [optional]  # noqa: E501
            mssql_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Msssql object.. [optional]  # noqa: E501
            netapp_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for NetApp object.. [optional]  # noqa: E501
            oracle_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Oracle object.. [optional]  # noqa: E501
            physical_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Physical object.. [optional]  # noqa: E501
            sharepoint_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for Sharepoint object.. [optional]  # noqa: E501
            uda_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for UDA object.. [optional]  # noqa: E501
            view_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters for a View.. [optional]  # noqa: E501
            vmware_params (VmwareObjectEntityParams): [optional]  # noqa: E501
            snapshot_tags ([SnapshotTagInfo], none_type): Specifies snapshot tags applied to the object.. [optional]  # noqa: E501
            tags ([TagInfo], none_type): Specifies tag applied to the object.. [optional]  # noqa: E501
            object_protection_infos ([ObjectProtectionInfo], none_type): Specifies the object info on each cluster.. [optional]  # noqa: E501
            source_info ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the Source Object information.. [optional]  # noqa: E501
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
              Object,
              SearchObjectAllOf,
              TagObject,
          ],
          'oneOf': [
          ],
        }

