# Gattaux Gabriel - 10/11/2025

import numpy as np
import cv2

class OpticLobes(object):
    def __init__(self,
                 target_px_scale,
                 sigma,
                 H_FOV,
                 V_FOV):
        
        self._target_px_scale = target_px_scale
        self._sigma = sigma
        self._H_FOV = H_FOV
        self._V_FOV = V_FOV

        print('Optic Lobes initialized !')
        
    def create_pn(self, img):
        """
        select channel/gray -> optional Gaussian blur -> optional resize -> optional Sobel magnitude.
        Returns float32 in [0,1].
        colormode: "gray", "blue", "green", "red" 
        target_px_scale: pixel scale desired
        """        
        # to float32 [0,1]
        g = img[:,:,2]

        # blur
        g = cv2.GaussianBlur(g, (0, 0), sigmaX=self._sigma, sigmaY=self._sigma, borderType=cv2.BORDER_REFLECT)

        # resize (keeps your original behavior using 360/target_hw and 90/target_hw)
        g = cv2.resize(g, (int(self._H_FOV/self._target_px_scale), int(self._V_FOV/self._target_px_scale)), interpolation=cv2.INTER_AREA)

        # sobel magnitude
        gx = cv2.Sobel(g, cv2.CV_32F, 1, 0, ksize=3, borderType=cv2.BORDER_REFLECT)
        gy = cv2.Sobel(g, cv2.CV_32F, 0, 1, ksize=3, borderType=cv2.BORDER_REFLECT)
        g = cv2.magnitude(gx, gy)

        RESO = self._H_FOV/self._target_px_scale
        x, y = np.meshgrid(np.arange(g.shape[0]), np.arange(g.shape[1]))
        # calculate distances from center of image
        dist = np.sqrt((x-(RESO/2))**2 + (y-(RESO/2))**2)
        # create boolean masks for radii
        outer_mask = dist <= RESO/2
        # apply masks to image
        vec = g[outer_mask]  #& inner_mas

        # vec = g.ravel()                    # 1D vector of circle (ring) pixels

        return g,vec