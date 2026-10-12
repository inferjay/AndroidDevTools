(function () {
    'use strict';

    const BATCH_SIZE = 24;
    const PLATFORMS = ['Windows', 'macOS', 'iOS', 'Android', 'Linux', 'Web'];
    const CATEGORIES = ['文件管理', '文档编辑', '效率日程', '影音媒体', '设计美学', '网络相关',
        '编程开发', '硬件管理', '系统优化', '安全防护', '学习教育', '生活工具'];

    function normalizeQuery(value) {
        return String(value || '').normalize('NFKC').trim().toLowerCase();
    }

    function filterProducts(products, query, platform, recommendedOnly, category) {
        const terms = normalizeQuery(query).split(/\s+/).filter(Boolean);
        return products.filter(function (product) {
            if (recommendedOnly && !product.isRecommended) {
                return false;
            }
            if (platform && platform !== 'all' && !(product.platforms || []).includes(platform)) {
                return false;
            }
            if (category && category !== 'all' && !(product.categories || []).includes(category)) {
                return false;
            }
            const text = normalizeQuery([product.name, product.fullName, product.description].join(' '));
            return terms.every(function (term) { return text.includes(term); });
        });
    }

    function formatPrice(price) {
        return (price / 100).toLocaleString('zh-CN', {
            minimumFractionDigits: price % 100 === 0 ? 0 : 2,
            maximumFractionDigits: 2
        });
    }

    function isWebUrl(value) {
        if (typeof value !== 'string' || !value) return false;
        try {
            const url = new URL(value);
            return url.protocol === 'https:' || url.protocol === 'http:';
        } catch (error) {
            return false;
        }
    }

    function validateCatalog(data) {
        if (!data || !Array.isArray(data.products) || !Number.isInteger(data.total) ||
            data.total !== data.products.length || typeof data.source !== 'string' ||
            typeof data.updatedAt !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(data.updatedAt)) {
            throw new Error('Invalid software catalog');
        }
        const ids = new Set();
        data.products.forEach(function (product) {
            if (!product || typeof product.id !== 'string' || !product.id || ids.has(product.id) ||
                typeof product.name !== 'string' || !product.name.trim() ||
                typeof product.fullName !== 'string' || typeof product.description !== 'string' ||
                !Array.isArray(product.platforms) || !product.platforms.every(function (platform) {
                    return PLATFORMS.includes(platform);
                }) || !Array.isArray(product.categories) || !product.categories.length ||
                new Set(product.categories).size !== product.categories.length ||
                !product.categories.every(function (category) { return CATEGORIES.includes(category); }) ||
                !['store', 'description'].includes(product.categorySource) ||
                !Number.isInteger(product.price) || product.price < 0 ||
                (product.originalPrice !== null &&
                    (!Number.isInteger(product.originalPrice) || product.originalPrice < 0)) ||
                !isWebUrl(product.url) || !isWebUrl(product.icon) ||
                (product.promotionImage !== null && !isWebUrl(product.promotionImage)) ||
                typeof product.isRecommended !== 'boolean' || typeof product.isOnSale !== 'boolean') {
                throw new Error('Invalid software product');
            }
            ids.add(product.id);
        });
        return true;
    }

    function createElement(document, tag, className, text) {
        const element = document.createElement(tag);
        if (className) element.className = className;
        if (text !== undefined) element.textContent = text;
        return element;
    }

    function createProductLink(document, product, className) {
        const link = createElement(document, 'a', className);
        const url = new URL(product.url);
        url.searchParams.set('cid', 'rmzbxelm');
        link.href = url.href;
        link.target = '_blank';
        link.rel = 'noopener sponsored';
        return link;
    }

    function createCard(document, product, index) {
        const card = createElement(document, 'li', 'software-card');
        card.dataset.productId = product.id;
        const article = createElement(document, 'article', 'software-card__article');
        const titleId = 'software-title-' + index;
        article.setAttribute('aria-labelledby', titleId);

        const media = createProductLink(document, product, 'software-card__media');
        media.setAttribute('aria-label', '去购买 ' + product.name + '（新窗口）');
        const image = createElement(document, 'img', 'software-card__image');
        image.alt = product.name;
        image.loading = 'lazy';
        image.decoding = 'async';
        let usingPromotion = Boolean(product.promotionImage);
        media.classList.add(usingPromotion ? 'software-card__media--promotion' : 'software-card__media--icon');

        image.addEventListener('error', function () {
            if (usingPromotion) {
                usingPromotion = false;
                media.classList.remove('software-card__media--promotion');
                media.classList.add('software-card__media--icon');
                image.src = product.icon;
            } else {
                const placeholder = createElement(document, 'span', 'software-card__placeholder', product.name);
                placeholder.setAttribute('role', 'img');
                placeholder.setAttribute('aria-label', product.name + '，图片暂不可用');
                media.replaceChildren(placeholder);
            }
        });
        image.src = product.promotionImage || product.icon;
        media.append(image);
        article.append(media);

        const content = createElement(document, 'div', 'software-card__content');
        const heading = createElement(document, 'h2', 'software-card__name');
        heading.id = titleId;
        const nameLink = createProductLink(document, product, 'software-card__name-link');
        nameLink.textContent = product.name;
        nameLink.title = product.fullName;
        heading.append(nameLink);
        content.append(heading);
        content.append(createElement(document, 'p', 'software-card__description', product.description || product.fullName));

        const tags = createElement(document, 'ul', 'software-card__platforms');
        tags.setAttribute('aria-label', '支持平台');
        product.platforms.forEach(function (platform) {
            tags.append(createElement(document, 'li', 'software-card__platform', platform));
        });
        if (product.isRecommended) {
            tags.append(createElement(document, 'li', 'software-card__platform software-card__platform--recommended', '推荐'));
        }
        if (product.platforms.length || product.isRecommended) content.append(tags);

        const footer = createElement(document, 'div', 'software-card__footer');
        const pricing = createElement(document, 'div', 'software-card__pricing');
        const currentPrice = createElement(document, 'span', 'software-card__price', '¥' + formatPrice(product.price));
        currentPrice.append(createElement(document, 'span', 'software-card__price-suffix', '起'));
        pricing.append(currentPrice);
        if (product.isOnSale && product.originalPrice !== null && product.originalPrice > product.price) {
            const originalPrice = createElement(document, 'del', 'software-card__original-price', '¥' + formatPrice(product.originalPrice));
            originalPrice.setAttribute('aria-label', '该套餐原价 ' + formatPrice(product.originalPrice) + ' 元');
            pricing.append(originalPrice);
        }
        footer.append(pricing);
        const action = createProductLink(document, product, 'software-card__action');
        action.textContent = '去购买';
        action.setAttribute('aria-label', '去购买 ' + product.name + '（新窗口）');
        footer.append(action);
        content.append(footer);
        article.append(content);
        card.append(article);
        return card;
    }

    function initialize(document) {
        const root = document.getElementById('software-catalog');
        if (!root) return;
        const search = document.getElementById('software-search');
        const clearSearch = document.getElementById('software-clear-search');
        const filters = document.getElementById('software-platform-filters');
        const platformButtons = Array.from(filters.querySelectorAll('button[data-platform]'));
        const recommendedButton = document.getElementById('software-recommended-filter');
        const categoryFilter = document.getElementById('software-category-filter');
        const grid = document.getElementById('software-grid');
        const count = document.getElementById('software-results-count');
        const metadata = document.getElementById('software-catalog-meta');
        const loading = document.getElementById('software-loading-state');
        const empty = document.getElementById('software-empty-state');
        const error = document.getElementById('software-error-state');
        const more = document.getElementById('software-load-more');
        const pagination = document.getElementById('software-pagination-status');
        let products = [];
        let matches = [];
        let platform = 'all';
        let recommendedOnly = false;
        let visibleCount = 0;
        let ready = false;

        function selectPlatform(value) {
            platform = value;
            platformButtons.forEach(function (button) {
                button.setAttribute('aria-pressed', String(button.dataset.platform === value));
            });
        }

        function selectRecommended(value) {
            recommendedOnly = value;
            recommendedButton.setAttribute('aria-pressed', String(value));
        }

        function renderBatch(reset, focusNewCard) {
            if (reset) {
                grid.replaceChildren();
                visibleCount = 0;
                matches = filterProducts(products, search.value, platform, recommendedOnly, categoryFilter.value);
            }
            const end = Math.min(visibleCount + BATCH_SIZE, matches.length);
            const fragment = document.createDocumentFragment();
            let firstNewLink;
            for (let index = visibleCount; index < end; index += 1) {
                const card = createCard(document, matches[index], index);
                if (!firstNewLink) firstNewLink = card.querySelector('.software-card__name-link');
                fragment.append(card);
            }
            grid.append(fragment);
            visibleCount = end;
            const remaining = matches.length - visibleCount;
            count.textContent = '找到 ' + matches.length + ' 款软件，已显示 ' + visibleCount + ' 款';
            empty.hidden = matches.length !== 0;
            grid.hidden = matches.length === 0;
            more.hidden = remaining === 0;
            more.textContent = remaining > BATCH_SIZE ? '显示更多（还有 ' + remaining + ' 款）' : '显示剩余 ' + remaining + ' 款';
            pagination.textContent = matches.length && !remaining ? '已显示全部 ' + matches.length + ' 款软件' : '';
            clearSearch.hidden = !search.value;
            if (focusNewCard && firstNewLink) firstNewLink.focus({ preventScroll: true });
        }

        function resetFilters() {
            search.value = '';
            selectPlatform('all');
            selectRecommended(false);
            categoryFilter.value = 'all';
            renderBatch(true);
            search.focus();
        }

        async function loadCatalog() {
            ready = false;
            root.setAttribute('aria-busy', 'true');
            search.disabled = true;
            filters.disabled = true;
            categoryFilter.disabled = true;
            loading.hidden = false;
            error.hidden = true;
            empty.hidden = true;
            grid.hidden = true;
            more.hidden = true;
            count.textContent = '正在加载软件目录…';
            pagination.textContent = '';
            try {
                const response = await fetch('static/data/software-picks.json', { cache: 'no-cache', credentials: 'omit' });
                if (!response.ok) throw new Error('Software catalog could not be loaded');
                const data = await response.json();
                validateCatalog(data);
                products = data.products;
                metadata.textContent = data.total + ' 款软件 · 更新于 ' + data.updatedAt;
                platformButtons.forEach(function (button) {
                    button.hidden = button.dataset.platform !== 'all' && !products.some(function (product) {
                        return product.platforms.includes(button.dataset.platform);
                    });
                });
                const selectedCategory = categoryFilter.value;
                const allCategories = createElement(document, 'option', null, '全部分类');
                allCategories.value = 'all';
                const categoryOptions = [allCategories];
                CATEGORIES.forEach(function (category) {
                    if (!products.some(function (product) { return product.categories.includes(category); })) return;
                    const option = createElement(document, 'option', null, category);
                    option.value = category;
                    categoryOptions.push(option);
                });
                categoryFilter.replaceChildren(...categoryOptions);
                categoryFilter.value = categoryOptions.some(function (option) {
                    return option.value === selectedCategory;
                }) ? selectedCategory : 'all';
                search.disabled = false;
                filters.disabled = false;
                categoryFilter.disabled = false;
                ready = true;
                renderBatch(true);
            } catch (failure) {
                count.textContent = '软件目录暂不可用';
                error.hidden = false;
            } finally {
                root.setAttribute('aria-busy', 'false');
                loading.hidden = true;
            }
        }

        search.addEventListener('input', function () {
            if (ready) renderBatch(true);
        });
        clearSearch.addEventListener('click', function () {
            search.value = '';
            if (ready) renderBatch(true);
            search.focus();
        });
        platformButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                if (!ready) return;
                selectPlatform(button.dataset.platform);
                renderBatch(true);
            });
        });
        recommendedButton.addEventListener('click', function () {
            if (!ready) return;
            selectRecommended(!recommendedOnly);
            renderBatch(true);
        });
        categoryFilter.addEventListener('change', function () {
            if (ready) renderBatch(true);
        });
        document.getElementById('software-reset-filters').addEventListener('click', resetFilters);
        document.getElementById('software-retry').addEventListener('click', loadCatalog);
        more.addEventListener('click', function () { renderBatch(false, true); });
        loadCatalog();
    }

    const api = { BATCH_SIZE: BATCH_SIZE, CATEGORIES: CATEGORIES, formatPrice: formatPrice,
        filterProducts: filterProducts, validateCatalog: validateCatalog };
    if (typeof module !== 'undefined' && module.exports) module.exports = api;
    if (typeof document !== 'undefined') initialize(document);
})();
