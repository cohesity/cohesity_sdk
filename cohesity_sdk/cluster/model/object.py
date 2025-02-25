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
    CommonNasObjectParams
    CommonObjectSummary
    FlashbladeObjectParams
    GroupObjectEntityParams
    IsilonObjectParams
    MongoDBObjectParams
    MssqlObjectEntityParams
    NetappObjectParams
    ObjectAllOf
    ObjectProtectionStatsSummary
    ObjectStringIdentifier
    ObjectSummary
    ObjectTypeVCenterParams
    ObjectTypeWindowsClusterParams
    OracleObjectEntityParams
    PermissionInfo
    PhysicalObjectEntityParams
    SharepointObjectEntityParams
    SharepointObjectParams
    UdaObjectParams
    ViewObjectParams
    VmwareObjectEntityParams


class Object(ModelComposed):
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
            'entity_id': (ObjectStringIdentifier,),  # noqa: E501
            'environment': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'source_id': (int,),  # noqa: E501
            'source_name': (str,),  # noqa: E501
            'child_objects': (list[ObjectSummary],),  # noqa: E501
            'global_id': (str,),  # noqa: E501
            'logical_size_bytes': (int,),  # noqa: E501
            'object_hash': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'os_type': (str,),  # noqa: E501
            'protection_type': (str,),  # noqa: E501
            'sharepoint_site_summary': (SharepointObjectParams,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'v_center_summary': (ObjectTypeVCenterParams,),  # noqa: E501
            'windows_cluster_summary': (ObjectTypeWindowsClusterParams,),  # noqa: E501
            'permissions': (PermissionInfo,),  # noqa: E501
            'protection_stats': (list[ObjectProtectionStatsSummary],),  # noqa: E501
            'elastifile_params': (CommonNasObjectParams,),  # noqa: E501
            'flashblade_params': (FlashbladeObjectParams,),  # noqa: E501
            'generic_nas_params': (CommonNasObjectParams,),  # noqa: E501
            'gpfs_params': (CommonNasObjectParams,),  # noqa: E501
            'group_params': (GroupObjectEntityParams,),  # noqa: E501
            'isilon_params': (IsilonObjectParams,),  # noqa: E501
            'mongo_db_params': (MongoDBObjectParams,),  # noqa: E501
            'mssql_params': (MssqlObjectEntityParams,),  # noqa: E501
            'netapp_params': (NetappObjectParams,),  # noqa: E501
            'oracle_params': (OracleObjectEntityParams,),  # noqa: E501
            'physical_params': (PhysicalObjectEntityParams,),  # noqa: E501
            'sharepoint_params': (SharepointObjectEntityParams,),  # noqa: E501
            'uda_params': (UdaObjectParams,),  # noqa: E501
            'view_params': (ViewObjectParams,),  # noqa: E501
            'vmware_params': (VmwareObjectEntityParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'entity_id': 'entityId',  # noqa: E501
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
        'mongo_db_params': 'mongoDBParams',  # noqa: E501
        'mssql_params': 'mssqlParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'oracle_params': 'oracleParams',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'sharepoint_params': 'sharepointParams',  # noqa: E501
        'uda_params': 'udaParams',  # noqa: E501
        'view_params': 'viewParams',  # noqa: E501
        'vmware_params': 'vmwareParams',  # noqa: E501
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
        """Object - a model defined in OpenAPI

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

            entity_id (ObjectStringIdentifier): [optional]  # noqa: E501
            environment (str): Specifies the environment of the object.. [optional]  # noqa: E501
            id (int): Specifies object id.. [optional]  # noqa: E501
            name (str): Specifies the name of the object.. [optional]  # noqa: E501
            source_id (int): Specifies registered source id to which object belongs.. [optional]  # noqa: E501
            source_name (str): Specifies registered source name to which object belongs.. [optional]  # noqa: E501
            child_objects (list[ObjectSummary]): Specifies child object details.. [optional]  # noqa: E501
            global_id (str): Specifies the global id which is a unique identifier of the object.. [optional]  # noqa: E501
            logical_size_bytes (int): Specifies the logical size of object in bytes.. [optional]  # noqa: E501
            object_hash (str): Specifies the hash identifier of the object.. [optional]  # noqa: E501
            object_type (str): Specifies the type of the object.. [optional]  # noqa: E501
            os_type (str): Specifies the operating system type of the object.. [optional]  # noqa: E501
            protection_type (str): Specifies the protection type of the object if any.. [optional]  # noqa: E501
            sharepoint_site_summary (SharepointObjectParams): [optional]  # noqa: E501
            uuid (str): Specifies the uuid which is a unique identifier of the object.. [optional]  # noqa: E501
            v_center_summary (ObjectTypeVCenterParams): [optional]  # noqa: E501
            windows_cluster_summary (ObjectTypeWindowsClusterParams): [optional]  # noqa: E501
            permissions (PermissionInfo): [optional]  # noqa: E501
            protection_stats (list[ObjectProtectionStatsSummary]): Specifies the count and size of protected and unprotected objects for the size.. [optional]  # noqa: E501
            elastifile_params (CommonNasObjectParams): [optional]  # noqa: E501
            flashblade_params (FlashbladeObjectParams): [optional]  # noqa: E501
            generic_nas_params (CommonNasObjectParams): [optional]  # noqa: E501
            gpfs_params (CommonNasObjectParams): [optional]  # noqa: E501
            group_params (GroupObjectEntityParams): [optional]  # noqa: E501
            isilon_params (IsilonObjectParams): [optional]  # noqa: E501
            mongo_db_params (MongoDBObjectParams): [optional]  # noqa: E501
            mssql_params (MssqlObjectEntityParams): [optional]  # noqa: E501
            netapp_params (NetappObjectParams): [optional]  # noqa: E501
            oracle_params (OracleObjectEntityParams): [optional]  # noqa: E501
            physical_params (PhysicalObjectEntityParams): [optional]  # noqa: E501
            sharepoint_params (SharepointObjectEntityParams): [optional]  # noqa: E501
            uda_params (UdaObjectParams): [optional]  # noqa: E501
            view_params (ViewObjectParams): [optional]  # noqa: E501
            vmware_params (VmwareObjectEntityParams): [optional]  # noqa: E501
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
              CommonObjectSummary,
              ObjectAllOf,
          ],
          'oneOf': [
          ],
        }

