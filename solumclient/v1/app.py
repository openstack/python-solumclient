# Copyright 2015 - Noorul Islam K M
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from solumclient.common.apiclient import base as apiclient_base
from solumclient.common.apiclient import exceptions
from solumclient.common import base as solum_base
from solumclient.common import exc

from oslo_utils import uuidutils


class App(apiclient_base.Resource):
    def __repr__(self):
        return "<App %s>" % self._info


class AppManager(solum_base.CrudManager, solum_base.FindMixin):
    resource_class = App
    collection_key = 'apps'
    key = 'app'

    def list(self, **kwargs):
        return super(AppManager, self).list(base_url="/v1", **kwargs)

    def create(self, **kwargs):
        return super(AppManager, self).create(base_url="/v1", **kwargs)

    def get(self, **kwargs):
        return super(AppManager, self).get(base_url="/v1", **kwargs)

    def put(self, **kwargs):
        return super(AppManager, self).put(base_url="/v1", **kwargs)

    def patch(self, **kwargs):
        return super(AppManager, self).patch(base_url="/v1", **kwargs)

    def delete(self, **kwargs):
        return super(AppManager, self).delete(base_url="/v1", **kwargs)

    def find(self, **kwargs):
        if 'app_id' in kwargs:
            return super(AppManager, self).get(base_url="/v1", **kwargs)
        elif 'name_or_id' in kwargs:
            name_or_uuid = kwargs['name_or_id']
            try:
                if uuidutils.is_uuid_like(name_or_uuid):
                    return super(AppManager, self).get(
                        base_url="/v1",
                        app_id=name_or_uuid)
                else:
                    return super(AppManager, self).findone(
                        name=name_or_uuid)
            except exceptions.NoUniqueMatch:
                raise exc.NotUnique(resource='App')
