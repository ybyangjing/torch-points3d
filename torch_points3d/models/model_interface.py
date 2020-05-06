from abc import abstractmethod, abstractproperty, ABC


class CheckpointInterface(ABC):
    """This class is a minimal interface class for models.
    """

    @abstractproperty  # type: ignore
    def schedulers(self):
        pass

    @schedulers.setter  # type: ignore
    @abstractmethod
    def schedulers(self, schedulers):
        pass

    @abstractproperty  # type: ignore
    def optimizer(self):
        pass

    @optimizer.setter  # type: ignore
    @abstractmethod
    def optimizer(self, optimizer):
        pass


class DatasetInterface(ABC):
    @abstractproperty
    def conv_type(self):
        pass

    def get_spatial_ops(self):
        pass


class TrackerInterface(ABC):
    @abstractmethod
    def get_labels(self):
        """ returns a trensor of size ``[N_points]`` where each value is the label of a point
        """

    @abstractmethod
    def get_batch_idx(self):
        """ returns a trensor of size ``[N_points]`` where each value is the batch index of a point
        """

    @abstractmethod
    def get_output(self):
        """ returns a trensor of size ``[N_points,...]`` where each value is the output
        of the network for a point (output of the last layer in general)
        """

    @abstractmethod
    def get_input(self):
        """ returns the last input that was given to the model or raises error
        """

    @abstractmethod
    def get_current_losses(self):
        """Return traning losses / errors. train.py will print out these errors on console"""