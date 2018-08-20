import keras
from keras_self_attention import Attention
from .util import TestMaskShape


class TestMul(TestMaskShape):

    def test_multiplicative(self):
        attention = Attention(return_attention=True,
                              attention_width=15,
                              attention_type=Attention.ATTENTION_TYPE_MUL,
                              kernel_regularizer=keras.regularizers.l2(1e-4),
                              bias_regularizer=keras.regularizers.l1(1e-4),
                              name='Attention')
        self.check_mask_shape(attention)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            Attention(return_attention=True,
                      attention_type='random')
