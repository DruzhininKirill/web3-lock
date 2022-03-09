import inject

from infrastructure.repositories import Repository

service = None


@inject.autoparams()
def get_lock_service(repo: Repository):
    global service
    if service is None:
        service = Web3LockService(repo)
    return service


class Web3LockService:
    @inject.autoparams()
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self.repository = repository

    async def get_lock_by_id(self, _id: str):
        return await self.repository.get_locks()


