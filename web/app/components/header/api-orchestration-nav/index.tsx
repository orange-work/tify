'use client'

import { useTranslation } from 'react-i18next'
import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'
import {
  Webhooks,
} from '@/app/components/base/icons/src/vender/line/development'
import classNames from '@/utils/classnames'
type ApiOrchestrationNavProps = {
  className?: string
}

const ApiOrchestrationNav = ({
  className,
}: ApiOrchestrationNavProps) => {
  const { t } = useTranslation()
  const selectedSegment = useSelectedLayoutSegment()
  const activated = selectedSegment === 'api-orchestration'

  return (
    <Link href="/api-orchestration" className={classNames(
      'group text-sm font-medium',
      activated && 'font-semibold bg-components-main-nav-nav-button-bg-active hover:bg-components-main-nav-nav-button-bg-active-hover shadow-md',
      activated ? 'text-components-main-nav-nav-button-text-active' : 'text-components-main-nav-nav-button-text hover:bg-components-main-nav-nav-button-bg-hover',
      className,
    )}>
      {
        <Webhooks className='mr-2 h-4 w-4' />
      }
      {t('common.menus.apiOrchestration')}
    </Link>
  )
}

export default ApiOrchestrationNav
