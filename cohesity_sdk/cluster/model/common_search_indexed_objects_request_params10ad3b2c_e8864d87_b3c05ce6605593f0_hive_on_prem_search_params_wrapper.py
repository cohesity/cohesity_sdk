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
    from cohesity_sdk.cluster.model.common_search_indexed_objects_request_params10ad3b2c_e8864d87_b3c05ce6605593f0 import CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0
    from cohesity_sdk.cluster.model.common_search_indexed_objects_request_params10ad3b2c_e8864d87_b3c05ce6605593f0_hive_on_prem_search_params_wrapper_all_of import CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapperAllOf
    from cohesity_sdk.cluster.model.hive_on_prem_search_params import HiveOnPremSearchParams
    globals()['CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0'] = CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0
    globals()['CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapperAllOf'] = CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapperAllOf
    globals()['HiveOnPremSearchParams'] = HiveOnPremSearchParams


class CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapper(ModelComposed):
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
        ('object_type',): {
            'EMAILS': "Emails",
            'FILES': "Files",
            'CASSANDRAOBJECTS': "CassandraObjects",
            'COUCHBASEOBJECTS': "CouchbaseObjects",
            'HBASEOBJECTS': "HbaseObjects",
            'HIVEOBJECTS': "HiveObjects",
            'MONGOOBJECTS': "MongoObjects",
            'HDFSOBJECTS': "HDFSObjects",
            'EXCHANGEOBJECTS': "ExchangeObjects",
            'PUBLICFOLDERS': "PublicFolders",
            'TEAMSOBJECTS': "TeamsObjects",
            'SHAREPOINTOBJECTS': "SharepointObjects",
            'ONEDRIVEOBJECTS': "OneDriveObjects",
            'UDAOBJECTS': "UdaObjects",
            'SFDCRECORDS': "SfdcRecords",
        },
    }

    validations = {
        ('tags',): {
        },

        ('must_have_tag_ids',): {
        },

        ('might_have_tag_ids',): {
        },

        ('must_have_snapshot_tag_ids',): {
        },

        ('might_have_snapshot_tag_ids',): {
        },

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
            'object_type': (str,),  # noqa: E501
            'protection_group_ids': ([str], none_type,),  # noqa: E501
            'storage_domain_ids': ([int], none_type,),  # noqa: E501
            'tenant_id': (str, none_type,),  # noqa: E501
            'include_tenants': (bool, none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
            'snapshot_tags': ([str],),  # noqa: E501
            'must_have_tag_ids': ([str], none_type,),  # noqa: E501
            'might_have_tag_ids': ([str], none_type,),  # noqa: E501
            'must_have_snapshot_tag_ids': ([str], none_type,),  # noqa: E501
            'might_have_snapshot_tag_ids': ([str], none_type,),  # noqa: E501
            'pagination_cookie': (str, none_type,),  # noqa: E501
            'count': (int, none_type,),  # noqa: E501
            'use_cached_data': (bool, none_type,),  # noqa: E501
            'hive_params': (HiveOnPremSearchParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'object_type': 'objectType',  # noqa: E501
        'protection_group_ids': 'protectionGroupIds',  # noqa: E501
        'storage_domain_ids': 'storageDomainIds',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
        'include_tenants': 'includeTenants',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'snapshot_tags': 'snapshotTags',  # noqa: E501
        'must_have_tag_ids': 'mustHaveTagIds',  # noqa: E501
        'might_have_tag_ids': 'mightHaveTagIds',  # noqa: E501
        'must_have_snapshot_tag_ids': 'mustHaveSnapshotTagIds',  # noqa: E501
        'might_have_snapshot_tag_ids': 'mightHaveSnapshotTagIds',  # noqa: E501
        'pagination_cookie': 'paginationCookie',  # noqa: E501
        'count': 'count',  # noqa: E501
        'use_cached_data': 'useCachedData',  # noqa: E501
        'hive_params': 'hiveParams',  # noqa: E501
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
    def __init__(self, object_type, *args, **kwargs):  # noqa: E501
        """CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapper - a model defined in OpenAPI

        Args:
            object_type (str): Specifies the object type to be searched for.

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

            protection_group_ids ([str], none_type): Specifies a list of Protection Group ids to filter the indexed objects. If specified, the objects indexed by specified Protection Group ids will be returned.. [optional]  # noqa: E501
            storage_domain_ids ([int], none_type): Specifies the Storage Domain ids to filter indexed objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains.. [optional]  # noqa: E501
            tenant_id (str, none_type): TenantId contains id of the tenant for which objects are to be returned.. [optional]  # noqa: E501
            include_tenants (bool, none_type): If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false.. [optional] if omitted the server will use the default value of False  # noqa: E501
            tags ([str], none_type): \"This field is deprecated. Please use mightHaveTagIds.\". [optional]  # noqa: E501
            snapshot_tags ([str]): \"This field is deprecated. Please use mightHaveSnapshotTagIds.\". [optional]  # noqa: E501
            must_have_tag_ids ([str], none_type): Specifies tags which must be all present in the document.. [optional]  # noqa: E501
            might_have_tag_ids ([str], none_type): Specifies list of tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query.. [optional]  # noqa: E501
            must_have_snapshot_tag_ids ([str], none_type): Specifies snapshot tags which must be all present in the document.. [optional]  # noqa: E501
            might_have_snapshot_tag_ids ([str], none_type): Specifies list of snapshot tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query.. [optional]  # noqa: E501
            pagination_cookie (str, none_type): Specifies the pagination cookie with which subsequent parts of the response can be fetched.. [optional]  # noqa: E501
            count (int, none_type): Specifies the number of indexed objects to be fetched for the specified pagination cookie.. [optional]  # noqa: E501
            use_cached_data (bool, none_type): Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source.. [optional]  # noqa: E501
            hive_params (HiveOnPremSearchParams): [optional]  # noqa: E501
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
            'object_type': object_type,
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
              CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0,
              CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HiveOnPremSearchParamsWrapperAllOf,
          ],
          'oneOf': [
          ],
        }

