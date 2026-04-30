# 晶格热容的量子理论

## 低温下热容的经验行为

当 $T \to 0$ 时，晶格热容满足：

$$
C_V \propto
\begin{cases}
T, & \text{金属中的电子热容} \\
T^3, & \text{绝缘体或半导体中的晶格热容}
\end{cases}
$$

本节主要讨论晶格振动对热容的贡献。

---

## 2. 谐振子的平均能量

晶格振动可以量子化为一组独立的谐振子。第 $i$ 个振动模的能量为：

$$
E_{n_i} = \left(n_i + \frac{1}{2}\right)\hbar\omega_i
$$

其中 $n_i = 0,1,2,\cdots$。

配分函数为：$Z_i = \sum_{n_i=0}^{\infty} e^{-\beta n_i \hbar \omega_i}$

其中：

$$
\beta = \frac{1}{k_B T}
$$

平均能量为：

$$
\bar{E}_i(T)
= \frac{1}{2}\hbar\omega_i
+ \frac{\sum_{n_i=0}^{\infty} n_i\hbar\omega_i e^{-\beta n_i\hbar\omega_i}}
{\sum_{n_i=0}^{\infty} e^{-\beta n_i\hbar\omega_i}}
$$

也可以写成：

$$
\bar{E}_i(T)
= \frac{1}{2}\hbar\omega_i
- \frac{\partial}{\partial\beta}
\ln\sum_{n_i=0}^{\infty} e^{-\beta n_i\hbar\omega_i}
$$

由于：

$$
\sum_{n_i=0}^{\infty} e^{-\beta n_i\hbar\omega_i}
=
\frac{1}{1-e^{-\beta\hbar\omega_i}}
$$

所以：

$$
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\frac{\hbar\omega_i}{e^{\beta\hbar\omega_i}-1}
$$

令平均声子数为：

$$
\bar{n}_i
=
\frac{1}{e^{\beta\hbar\omega_i}-1}
$$

则：

$$
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\bar{n}_i\hbar\omega_i
$$

第一项是零点能，第二项是热激发声子的平均能量。

---

## 3. 单个振动模的热容

单个振动模对热容的贡献为：

$$
C_{V,i}
=
\frac{\partial \bar{E}_i}{\partial T}
$$

由：

$$
\bar{E}_i(T)
=
\frac{1}{2}\hbar\omega_i
+
\frac{\hbar\omega_i}{e^{\hbar\omega_i/k_B T}-1}
$$

可以得到：

$$
C_{V,i}
=
k_B
\frac{
\left(\frac{\hbar\omega_i}{k_B T}\right)^2
e^{\hbar\omega_i/k_B T}
}{
\left(e^{\hbar\omega_i/k_B T}-1\right)^2
}
$$

低温极限下，当 $k_B T \ll \hbar\omega_i$ 时：

$$
C_{V,i}
\approx
k_B
\left(\frac{\hbar\omega_i}{k_B T}\right)^2
e^{-\hbar\omega_i/k_B T}
\to 0
$$

高温极限下，当 $k_B T \gg \hbar\omega_i$ 时：

$$
C_{V,i}
\to k_B
$$

这就是每个谐振子在高温下给出 $k_B$ 的热容贡献。

---

## 4. Einstein 模型

Einstein 模型假设晶体中所有原子都以相同频率 $\omega_E$ 振动。

对于含有 $N$ 个原子的晶体，总共有 $3N$ 个振动自由度，因此：

$$
C_V
=
3N k_B
\frac{
\left(\frac{\hbar\omega_E}{k_B T}\right)^2
e^{\hbar\omega_E/k_B T}
}{
\left(e^{\hbar\omega_E/k_B T}-1\right)^2
}
$$

定义 Einstein 温度：

$$
\theta_E = \frac{\hbar\omega_E}{k_B}
$$

则：

$$
C_V
=
3N k_B
\frac{
\left(\frac{\theta_E}{T}\right)^2
e^{\theta_E/T}
}{
\left(e^{\theta_E/T}-1\right)^2
}
$$

高温极限：

$$
T \gg \theta_E
$$

此时：

$$
C_V \to 3N k_B
$$

这对应 Dulong--Petit 定律。

低温极限：

$$
T \ll \theta_E
$$

此时：

$$
C_V
\approx
3N k_B
\left(\frac{\theta_E}{T}\right)^2
e^{-\theta_E/T}
\to 0
$$

Einstein 模型可以解释低温热容趋于零，但它给出的是指数衰减，而实验中许多绝缘体低温下满足：

$$
C_V \propto T^3
$$

因此需要 Debye 模型。

---

## 5. Debye 模型

Debye 模型把晶格振动看成连续介质中的弹性波。声学支近似满足线性色散关系：

$$
\omega = c q
$$

其中 $c$ 是声速。

对于纵波和横波，声速一般不同：

$$
\omega = c_l q
$$

$$
\omega = c_t q
$$

其中 $c_l$ 是纵波声速，$c_t$ 是横波声速。

在三维中，一个波矢态在 $q$ 空间中占据的体积为：

$$
\frac{(2\pi)^3}{V}
$$

因此 $q$ 空间中的态密度因子为：

$$
\frac{V}{(2\pi)^3}
$$

---

## 6. 振动态密度

一般地，振动态密度定义为：

$$
g(\omega) = \frac{dn}{d\omega}
$$

更一般地，可以写成等频面上的积分：

$$
g(\omega)
=
\frac{V}{(2\pi)^3}
\int
\frac{dS}{\left|\frac{d\omega}{dq}\right|}
$$

其中 $dS$ 是 $q$ 空间中等频面上的面积元。

### 一维情况

一维中，若：

$$
\omega = c q
$$

则：

$$
g(\omega) \propto \frac{1}{c}
$$

所以一维线性色散下：

$$
g(\omega) \propto \omega^0
$$

### 二维情况

二维中等频线是圆，长度为：

$$
2\pi q
$$

若：

$$
\omega = c q
$$

则：

$$
g(\omega) \propto q \frac{dq}{d\omega}
$$

因为：

$$
q = \frac{\omega}{c}
$$

所以：

$$
g(\omega) \propto \omega
$$

### 三维情况

三维中等频面是球面，面积为：

$$
4\pi q^2
$$

若：

$$
\omega = c q
$$

则：

$$
g(\omega)
=
\frac{V}{(2\pi)^3}
4\pi q^2
\frac{dq}{d\omega}
$$

因为：

$$
q = \frac{\omega}{c},
\qquad
\frac{dq}{d\omega} = \frac{1}{c}
$$

所以：

$$
g(\omega)
=
\frac{V}{2\pi^2 c^3}\omega^2
$$

如果考虑三支声学支，并且简化为同一声速 $c$，则：

$$
g(\omega)
=
\frac{3V}{2\pi^2 c^3}\omega^2
$$

如果区分一支纵波和两支横波，则：

$$
g(\omega)
=
\frac{V\omega^2}{2\pi^2}
\left(
\frac{1}{c_l^3}
+
\frac{2}{c_t^3}
\right)
$$

---

## 7. Debye 截止频率

Debye 模型假设声子频率只到某个最大频率 $\omega_D$，并要求总振动模数为 $3N$：

$$
\int_0^{\omega_D} g(\omega)\,d\omega = 3N
$$

定义 Debye 温度：

$$
\theta_D = \frac{\hbar\omega_D}{k_B}
$$

---

## 8. Debye 热容公式

总热容可以写成对所有频率的积分：

$$
C_V(T)
=
k_B
\int_0^{\omega_D}
\frac{
\left(\frac{\hbar\omega}{k_B T}\right)^2
e^{\hbar\omega/k_B T}
}{
\left(e^{\hbar\omega/k_B T}-1\right)^2
}
g(\omega)\,d\omega
$$

对于三维 Debye 模型，最终得到：

$$
C_V
=
9N k_B
\left(\frac{T}{\theta_D}\right)^3
\int_0^{\theta_D/T}
\frac{x^4 e^x}{(e^x-1)^2}\,dx
$$

其中：

$$
x = \frac{\hbar\omega}{k_B T}
$$

---

## 9. Debye 模型的高温与低温极限

### 高温极限

当：

$$
T \gg \theta_D
$$

有：

$$
C_V \to 3N k_B
$$

即 Dulong--Petit 定律。

### 低温极限

当：

$$
T \ll \theta_D
$$

积分上限可以近似为无穷大：

$$
\frac{\theta_D}{T} \to \infty
$$

因此：

$$
C_V
\propto
T^3
$$

更具体地：

$$
C_V
\approx
\frac{12\pi^4}{5}
N k_B
\left(\frac{T}{\theta_D}\right)^3
$$

这说明三维晶体在低温下的晶格热容满足：

$$
C_V \sim T^3
$$

这就是 Debye $T^3$ 定律。

---

## 10. 不同维度下的低温热容

若声学声子的低频色散为线性：

$$
\omega = c q
$$

则在 $d$ 维中，低频振动态密度满足：

$$
g(\omega) \propto \omega^{d-1}
$$

因此低温热容满足：

$$
C_V \propto T^d
$$

所以：

$$
\begin{aligned}
\text{一维：} \quad & C_V \propto T \\
\text{二维：} \quad & C_V \propto T^2 \\
\text{三维：} \quad & C_V \propto T^3
\end{aligned}
$$

---

## 11. 非线性色散关系的情况

如果色散关系不是线性的，例如：

$$
\omega = c q^s
$$

则：

$$
q = \left(\frac{\omega}{c}\right)^{1/s}
$$

振动态密度的频率依赖会发生变化。一般地，在 $d$ 维中：

$$
g(\omega) \propto \omega^{\frac{d}{s}-1}
$$

因此低温热容满足：

$$
C_V \propto T^{d/s}
$$

例如，在二维中如果存在二次色散关系：

$$
\omega \propto q^2
$$

则：

$$
g(\omega) \propto \omega^0
$$

并且：

$$
C_V \propto T
$$

---

## 12. 一维单原子链的态密度

对于一维单原子链，色散关系为：

$$
\omega(q)
=
\omega_m
\left|\sin\frac{qa}{2}\right|
$$

其中：

$$
\omega_m = \sqrt{\frac{4\beta}{m}}
$$

在第一布里渊区中，$q$ 的取值范围长度为：

$$
\Delta q = \frac{2\pi}{Na}
$$

由态密度关系：

$$
g(\omega)
\propto
\frac{1}{\left|\frac{d\omega}{dq}\right|}
$$

又有：

$$
\frac{d\omega}{dq}
=
\frac{a}{2}
\sqrt{\omega_m^2-\omega^2}
$$

因此：

$$
g(\omega)
\propto
\frac{1}{\sqrt{\omega_m^2-\omega^2}}
$$

更具体地可写为：

$$
g(\omega)
=
\frac{2N}{\pi}
\frac{1}{\sqrt{\omega_m^2-\omega^2}}
$$

这个结果说明，在一维单原子链中，态密度在带边 $\omega \to \omega_m$ 附近会发散。